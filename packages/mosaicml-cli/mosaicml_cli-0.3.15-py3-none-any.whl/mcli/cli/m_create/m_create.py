""" mcli create Commands """
import argparse
import logging
import textwrap

from mcli.cli.m_create.cluster import CLUSTER_EXAMPLES, configure_cluster_argparser, create_new_cluster
from mcli.cli.m_create.env_var import configure_env_var_argparser, create_new_env_var
from mcli.cli.m_create.secret import configure_secret_argparser, create_new_secret
from mcli.config import FeatureFlag, MCLIConfig

logger = logging.getLogger(__name__)


def create(**kwargs) -> int:
    del kwargs
    mock_parser = configure_argparser(parser=argparse.ArgumentParser())
    mock_parser.print_help()
    return 0


def add_common_arguments(parser: argparse.ArgumentParser):
    parser.add_argument('--no-input', action='store_true', help='Do not query for user input')


def configure_argparser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    conf = MCLIConfig.load_config(safe=True)

    subparsers = parser.add_subparsers(title='MCLI Objects',
                                       description='The table below shows the objects that you can create',
                                       help='DESCRIPTION',
                                       metavar='OBJECT')
    parser.set_defaults(func=create)

    if not conf.feature_enabled(FeatureFlag.USE_MCLOUD):
        # pylint: disable=invalid-name
        CLUSTER_DESC = textwrap.dedent("""
                                        Add a new cluster in which you can launch runs. If you do not know the appropriate
                                        context, running `mcli create cluster` alone will give you a list of options to
                                        choose from.""")

        cluster_parser = subparsers.add_parser('cluster',
                                               aliases=['clusters', 'platforms', "platform"],
                                               help='Add a cluster to launch runs in',
                                               description=CLUSTER_DESC,
                                               epilog=CLUSTER_EXAMPLES,
                                               formatter_class=argparse.RawDescriptionHelpFormatter)
        configure_cluster_argparser(cluster_parser)
        add_common_arguments(cluster_parser)
        cluster_parser.set_defaults(func=create_new_cluster)

        environment_parser = subparsers.add_parser(
            'env',
            aliases=['envs'],
            help='Create environment variables to use across your runs',
            description='Setup environment variables that will be used in all of your subsequent workloads',
        )
        configure_env_var_argparser(environment_parser)
        add_common_arguments(environment_parser)
        environment_parser.set_defaults(func=create_new_env_var)

    # pylint: disable-next=invalid-name
    SECRET_EXAMPLES = textwrap.dedent("""

    Examples:

    # Create an "env" (environment variable) secret
    mcli create secret env FOO=super-secret-api-key-1234
    """)
    secrets_parser = subparsers.add_parser(
        'secret',
        aliases=['secrets'],
        help='Create secrets and credentials to add to your runs',
        description='Add secrets and credentials that will be added to all of your '
        'subsequent runs. For details on exactly how each type of secret is added to '
        'your run, look to the individual secret type docs.',
        epilog=SECRET_EXAMPLES,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    configure_secret_argparser(secrets_parser, secret_handler=create_new_secret)
    # Secret creation only happens through subparsers, so just print help if a subparser isn't specified
    secrets_parser.set_defaults(func=lambda **kwargs: secrets_parser.print_help())

    return parser


def add_create_argparser(subparser: argparse._SubParsersAction,) -> argparse.ArgumentParser:
    create_parser: argparse.ArgumentParser = subparser.add_parser(
        'create',
        help='Create an MCLI object. See `mcli create -h` for available objects',
        description='Create an MCLI object. These objects assist in running your workloads in various ways.',
    )
    create_parser = configure_argparser(parser=create_parser)
    return create_parser
