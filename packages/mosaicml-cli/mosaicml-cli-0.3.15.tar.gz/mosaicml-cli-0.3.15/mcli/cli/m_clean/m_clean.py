""" mcli clean Entrypoint """
import os
import shutil

from mcli import config
from mcli.utils.utils_interactive import query_yes_no


def clean_mcli(**kwargs) -> int:
    del kwargs
    if not os.path.exists(config.MCLI_CONFIG_DIR):
        print('Already clean!')
        return 1

    if not query_yes_no(
            message='Are you sure you want to clean up your MCLI Configs?\n'
            f' This is a destructive action!\nA backup will be saved at {config.MCLI_BACKUP_CONFIG_DIR}:',
            default=False,
    ):
        print('Exiting...')
        return 1

    if os.path.exists(config.MCLI_BACKUP_CONFIG_DIR):
        if not query_yes_no(message='A current backup exists, overwrite it?:'):
            print('Exiting...')
            return 1
        else:
            shutil.rmtree(config.MCLI_BACKUP_CONFIG_DIR)
    shutil.move(str(config.MCLI_CONFIG_DIR), str(config.MCLI_BACKUP_CONFIG_DIR))

    print('All clean!')
    return 0
