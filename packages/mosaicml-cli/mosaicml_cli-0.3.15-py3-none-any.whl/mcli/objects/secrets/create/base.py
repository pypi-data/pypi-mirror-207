"""Base creator for secrets"""
import logging
import uuid
from typing import Callable, List, Optional, Set

from mcli.api.exceptions import ValidationError
from mcli.config import FeatureFlag, MCLIConfig
from mcli.models import Cluster, Secret, SecretType
from mcli.objects.secrets import SECRET_CLASS_MAP
from mcli.objects.secrets.cluster_secret import SecretManager
from mcli.utils.utils_interactive import simple_prompt
from mcli.utils.utils_logging import FAIL
from mcli.utils.utils_string_functions import validate_secret_name

logger = logging.getLogger(__name__)


class SecretValidationError(ValidationError):
    """Secret could not be configured with the provided values
    """


class SecretFiller():
    """Interactive filler for secret data
    """

    @staticmethod
    def fill_name(validate: Callable[[str], bool]) -> str:
        return simple_prompt('What would you like to name this secret?', validate=validate)


class SecretValidator():
    """Validation methods for secret data

    Raises:
        SecretValidationError: Raised for any validation error for secret data
    """

    def __init__(self):
        conf = MCLIConfig.load_config(safe=True)
        if conf.feature_enabled(FeatureFlag.USE_MCLOUD):
            self.existing_secrets = []
            self.existing_secret_names = set()
        else:
            self.validate_one_cluster_exists(conf.clusters)
            secret_manager = SecretManager(conf.clusters[0])
            self.existing_secrets = [ps.secret for ps in secret_manager.get_secrets()]
            self.existing_secret_names = {secret.name for secret in self.existing_secrets}

        super().__init__()

    @staticmethod
    def validate_one_cluster_exists(clusters: List[Cluster]) -> bool:

        if not clusters:
            raise SecretValidationError(
                'No clusters found. You must have at least one cluster setup before you add secrets. '
                'Please try running `mcli create cluster` first to generate one.')
        return True

    @staticmethod
    def validate_secret_name_available(name: str, existing_names: Set[str]) -> bool:
        if name in existing_names:
            raise SecretValidationError(f'Existing secret. Secret named {name} already exists. Please choose '
                                        f'something not in {sorted(list(existing_names))}.')
        return True

    @staticmethod
    def validate_secret_name_rfc(name: str) -> bool:

        result = validate_secret_name(name)
        if not result:
            raise SecretValidationError(result.message)
        return True

    def validate_secret_name_full(self, name: str) -> bool:
        return self.validate_secret_name_rfc(name) and self.validate_secret_name_available(
            name, self.existing_secret_names)


class SecretCreator(SecretValidator, SecretFiller):
    """Creates base secrets for the CLI
    """

    @staticmethod
    def create_base_secret(name: str, secret_type: SecretType) -> Secret:
        secret_class = SECRET_CLASS_MAP.get(secret_type)
        if not secret_class:
            raise SecretValidationError(f'{FAIL} The secret type: {secret_type} does not exist.')

        return secret_class(name, secret_type)

    def create(self,
               secret_type: SecretType,
               name: Optional[str] = None,
               make_name_unique: bool = False,
               **kwargs) -> Secret:

        del kwargs

        if name:
            try:
                self.validate_secret_name_available(name, self.existing_secret_names)
            except SecretValidationError:
                if make_name_unique:
                    name = f'{name[:58]}-{str(uuid.uuid4())[:4]}'
                else:
                    raise
            self.validate_secret_name_rfc(name)

        if not name:
            name = self.fill_name(validate=self.validate_secret_name_full)

        return self.create_base_secret(name, secret_type)
