""" MCLI Git Repo Integration """
import logging
from dataclasses import dataclass
from typing import Optional

from mcli.models import MCLIIntegration
from mcli.serverside.job.mcli_k8s_job import MCLIK8sJob

logger = logging.getLogger(__name__)


@dataclass
class MCLIGitRepoIntegration(MCLIIntegration):
    """Git Repository Integration
    """
    git_repo: str
    git_branch: Optional[str] = None
    git_commit: Optional[str] = None
    path: Optional[str] = None
    ssh_clone: Optional[bool] = True
    pip_install: Optional[str] = None
    host: str = 'github.com'
    git_clone_recursive: Optional[bool] = False

    def add_to_job(self, kubernetes_job: MCLIK8sJob) -> bool:
        if self.git_commit and self.git_branch:
            logger.warning('Both git_commit and git_branch are provided, using git_commit.')

        clone_command = 'git clone '
        if self.git_clone_recursive:
            clone_command += ' --recursive'
        if self.git_branch and not self.git_commit:
            clone_command += f' -b {self.git_branch}'

        if self.ssh_clone:
            clone_command += f' git@{self.host}:{self.git_repo}.git'
        else:
            clone_command += f' https://{self.host}/{self.git_repo}.git'

        clone_path = self.path
        if self.path is None:
            repo_split = self.git_repo.split('/')
            assert len(repo_split) == 2, 'Git repos should have the form organization/repo'
            clone_path = repo_split[1]

        clone_command += f' {clone_path}'

        if self.git_commit:
            clone_command += f' && cd {clone_path} && git checkout {self.git_commit} && cd -'

        if self.pip_install:
            pip_install_command = f'pip install {self.pip_install}'
            full_pip_install_command = f'cd {clone_path} && {pip_install_command} && cd -'
            kubernetes_job.add_command(
                full_pip_install_command,
                error_message=f'Unable to install the repo with: {pip_install_command}',
                required=True,
            )

        kubernetes_job.add_command(
            clone_command,
            error_message=f'Unable to clone git repo: {self.git_repo}',
            required=True,
        )

        batch_mode_cmd = 'export GIT_SSH_COMMAND=${GIT_SSH_COMMAND:-"ssh -o StrictHostKeyChecking=no"}'
        if self.ssh_clone:
            kubernetes_job.add_command(batch_mode_cmd,
                                       error_message='Failed to set GIT_SSH_COMMAND to ignore host key checks',
                                       required=True)

        return True
