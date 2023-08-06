""" mcli create env Entrypoint """
import argparse
import logging
import re
from typing import Callable, Dict, List, Optional, Set

from mcli.api.exceptions import InputDisabledError, ValidationError
from mcli.config import MESSAGE, FeatureFlag, MCLIConfig, MCLIConfigError
from mcli.models import MCLIEnvVar
from mcli.objects.secrets.cluster_secret import SecretManager
from mcli.objects.secrets.env_var import MCLIEnvVarSecret
from mcli.utils.utils_interactive import input_disabled, simple_prompt
from mcli.utils.utils_logging import FAIL, OK
from mcli.utils.utils_string_functions import KEY_VALUE_PATTERN, validate_env_key, validate_key_value_pair

logger = logging.getLogger(__name__)
INPUT_DISABLED_MESSAGE = ('Incomplete environment variable. Please provide a name, key and value if running with '
                          '`--no-input`. Check `mcli create env --help` for more information.')


class EnvVarValidationError(ValidationError):
    """Env var could not be configured with the provided values
    """


class EnvVarFiller():
    """Interactive filler for environment variable data
    """

    @staticmethod
    def _fill_any(text: str, validate: Callable[[str], bool]) -> str:
        return simple_prompt(text, validate=validate)

    @classmethod
    def fill_name(cls, validate: Callable[[str], bool]) -> str:
        return cls._fill_any('What would you like to call this environment variable?', validate)

    @classmethod
    def fill_key(cls, validate: Callable[[str], bool]) -> str:
        return cls._fill_any('If the environment variable is KEY=VALUE, what should its KEY be?', validate)

    @classmethod
    def fill_value(cls) -> str:
        return cls._fill_any('If the environment variable is KEY=VALUE, what should its VALUE be?', lambda x: True)


class EnvVarValidator():
    """Validation methods for environment variable data

    Raises:
        EnvVarValidationError: Raised for any validation error for environment variable data
    """

    def __init__(self):
        super().__init__()
        self.existing_keys = self.get_existing_keys()

    def get_existing_secret_keys(self, conf: MCLIConfig) -> Set[str]:
        """Get keys from existing environment variable secrets

        Args:
            conf: MCLIConfig

        Returns:
            Set of env var keys

        TODO: This should include ALL env var keys added by other secrets + an exclude list from job creation
        """
        if not conf.clusters:
            return set()
        ref_cluster = conf.clusters[0]
        secret_manager = SecretManager(ref_cluster)
        keys = set()
        for cluster_secret in secret_manager.get_secrets():
            if isinstance(cluster_secret.secret, MCLIEnvVarSecret) and cluster_secret.secret.key:
                keys.add(cluster_secret.secret.key)

        return keys

    def get_existing_keys(self) -> Set[str]:
        conf = MCLIConfig.load_config(safe=True)
        if conf.feature_enabled(FeatureFlag.USE_MCLOUD):
            return set()

        env_keys = {ev.key for ev in conf.environment_variables}
        secret_keys = self.get_existing_secret_keys(conf)
        return env_keys | secret_keys

    @staticmethod
    def validate_env_pair(env_pair: str) -> bool:
        if not validate_key_value_pair(env_pair):
            raise EnvVarValidationError(
                'Environment variable must be specified like KEY=VALUE, where KEY must include only characters '
                f'in [0-9A-Za-z_]. Got: {env_pair}')
        return True

    @staticmethod
    def validate_key_valid(key: str) -> bool:
        if not validate_env_key(key):
            raise EnvVarValidationError('Invalid environment variable. Can only contain the characters [0-9A-Za-z_]')
        return True

    def validate_env_key_available(self, key: str) -> bool:
        if key in self.existing_keys:
            raise EnvVarValidationError(f'Existing environment key. Key named {key} already exists. Please '
                                        f'choose something not in {sorted(list(self.existing_keys))}')
        return True

    def validate_key(self, key: str) -> bool:
        return self.validate_key_valid(key) and self.validate_env_key_available(key)


class EnvVarCreator(EnvVarValidator, EnvVarFiller):
    """Creates environment variables for the CLI
    """

    def get_env_dict(self, env_pairs: Optional[List[str]] = None) -> Dict[str, str]:
        env_dict = {}
        if env_pairs is None:
            return env_dict

        for env_pair in env_pairs:
            self.validate_env_pair(env_pair)
            m = re.fullmatch(KEY_VALUE_PATTERN, env_pair)
            assert m is not None
            key, value = m.groups()
            if key in env_dict:
                raise EnvVarValidationError(f'Duplicate environment keys provided. Each environment variable key '
                                            f'should be unique but {key} was duplicated.')
            env_dict[key] = value
        return env_dict

    def create(self, env_pairs: Optional[List[str]] = None) -> List[MCLIEnvVar]:

        # Parse env pairs
        env_dict = self.get_env_dict(env_pairs)

        # Validate env keys
        for key in env_dict:
            self.validate_env_key_available(key)

        # Fill in missing values
        if not env_dict:
            key = self.fill_key(validate=self.validate_key)
            env_dict[key] = self.fill_value()

        return [MCLIEnvVar(key=key, value=value) for key, value in env_dict.items()]


def create_new_env_var(
    env_pairs: Optional[List[str]] = None,
    no_input: bool = False,
    **kwargs,
) -> int:
    """Create an environment variable

    All required variables can be provided directly. If they are not provided, they will
    be requested interactively from the user unless `no_input` is `True`.

    Args:
        variable_name: Name of the environment variable. Defaults to None.
        key: Environment variable key. Defaults to None.
        value: Environment variable value. Defaults to None.
        no_input: If True, all required data must be provided since no interactive user
            input is allowed. Defaults to False.

    Returns:
        0 if creation succeeded, else 1
    """
    del kwargs

    with input_disabled(no_input):
        try:
            creator = EnvVarCreator()
            new_env_vars = creator.create(env_pairs)
        except MCLIConfigError:
            logger.error(MESSAGE.MCLI_NOT_INITIALIZED)
            return 1
        except InputDisabledError:
            logger.error(INPUT_DISABLED_MESSAGE)
            return 1
        except EnvVarValidationError as e:
            logger.error(f'{FAIL} {e}')
            return 1

        conf: MCLIConfig = MCLIConfig.load_config()
        conf.environment_variables.extend(new_env_vars)
        conf.save_config()
        logger.info(f'{OK} Created environment variable(s): {",".join([ev.key for ev in new_env_vars])}')

    return 0


def configure_env_var_argparser(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        'env_pairs',
        nargs='*',
        help='A list of KEY=VALUE pairs',
    )
