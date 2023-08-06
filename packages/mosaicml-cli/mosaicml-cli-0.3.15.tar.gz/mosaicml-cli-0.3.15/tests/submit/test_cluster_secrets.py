""" Test secret interactions with Kubernetes """

from dataclasses import asdict
from typing import Any, Dict, List, Union

import pytest
from kubernetes import client

from mcli.models import Secret, SecretType
from mcli.objects.secrets import (MCLIDockerRegistrySecret, MCLIEnvVarSecret, MCLIGCPSecret, MCLIMountedSecret,
                                  MCLIS3Secret, MCLISSHSecret, SecretType)
from mcli.objects.secrets.cluster_secret import ClusterSecret
from mcli.objects.secrets.oci import MCLIOCISecret
from mcli.objects.secrets.ssh import MCLIGitSSHSecret
from mcli.serverside.job.mcli_k8s_job import MCLIK8sJob

SECRETS: Dict[SecretType, Secret] = {
    SecretType.docker_registry:
        MCLIDockerRegistrySecret(
            name='test-secret',
            secret_type=SecretType.docker_registry,
            username='test-user',
            password='pass123',
            email='testuser@123.com',
            server='testserver.com',
        ),
    SecretType.mounted:
        MCLIMountedSecret(
            name='test-secret',
            secret_type=SecretType.mounted,
            value='bar',
            mount_path='/secrets/test-secret',
        ),
    SecretType.ssh:
        MCLISSHSecret(
            name='test-secret',
            secret_type=SecretType.ssh,
            value='super-secret-ssh-key',
            mount_path='/secrets/test-secret',
        ),
    SecretType.git:
        MCLIGitSSHSecret(
            name='test-secret',
            secret_type=SecretType.git,
            value='super-secret-ssh-key',
            mount_path='/secrets/test-secret',
        ),
    SecretType.environment:
        MCLIEnvVarSecret(
            name='test-secret',
            secret_type=SecretType.environment,
            value='bar',
            key='FOO',
        ),
    SecretType.s3:
        MCLIS3Secret(
            name='test-secret',
            secret_type=SecretType.s3,
            mount_directory='/secrets/test-secret',
            credentials='SOME CRED',
            config='SOME CONFIG',
        ),
    SecretType.oci:
        MCLIOCISecret(name='test-secret',
                      secret_type=SecretType.oci,
                      mount_directory='/secrets/test-secret',
                      config='some config',
                      key_file='some key'),
    SecretType.gcp:
        MCLIGCPSecret(
            name='test-secret',
            secret_type=SecretType.gcp,
            mount_path='/secrets/test-secret',
            value='SOME CRED',
        ),
}


@pytest.fixture
def mcli_job():
    job = MCLIK8sJob.empty('test')
    job.container.image = 'alpine'
    job.container.command = ['sleep', 'infinity']
    return job


def get_kube_spec(kube_obj: Any) -> Union[List[Any], Dict[str, Any]]:
    api_client = client.ApiClient()
    return api_client.sanitize_for_serialization(kube_obj)


# Test docker secrets added
def test_docker_secret_add_to_job(mcli_job):

    secret = SECRETS[SecretType.docker_registry]
    assert isinstance(secret, MCLIDockerRegistrySecret)
    secret.add_to_job(mcli_job)

    # Check image pull secrets
    pull_secrets_spec = get_kube_spec(mcli_job.pod_spec.image_pull_secrets)
    assert pull_secrets_spec == [{'name': 'test-secret'}]


def check_volume_and_mount(secret: MCLIMountedSecret, mcli_job: MCLIK8sJob):
    """Check that volumes and mounts are set for the given secret in the job
    """
    assert secret.mount_path is not None

    # Check volumes
    volumes_spec = get_kube_spec(mcli_job.pod_volumes)
    assert isinstance(volumes_spec, list)

    v = volumes_spec[0]
    assert v['name'] == secret.name
    assert v['secret']['secretName'] == secret.name
    assert v['secret']['items'][0]['key'] == 'value'
    assert v['secret']['items'][0]['path'] == 'secret'

    # Check mounts
    mounts_spec = get_kube_spec(mcli_job.container_volume_mounts)
    assert isinstance(mounts_spec, list)

    m = mounts_spec[0]
    assert m['name'] == secret.name
    assert m['mountPath'] == secret.mount_path

    # Check mount path env var
    env_spec = get_kube_spec(mcli_job.environment_variables)
    assert isinstance(env_spec, list)

    ev = env_spec[0]
    assert ev['name'] == f'SECRET_PATH_{secret.name.upper().replace("-", "_")}'
    assert ev['value'] == str(f'{secret.mount_path}/secret')


# Test mounted secrets added
def test_mounted_secret_add_to_job(mcli_job: MCLIK8sJob):

    secret = SECRETS[SecretType.mounted]
    assert isinstance(secret, MCLIMountedSecret)
    secret.add_to_job(mcli_job)
    check_volume_and_mount(secret, mcli_job)


# Test SSH secrets added
def test_ssh_secret_add_to_job(mcli_job: MCLIK8sJob):

    secret = SECRETS[SecretType.ssh]
    assert isinstance(secret, MCLISSHSecret)
    secret.add_to_job(mcli_job)
    check_volume_and_mount(secret, mcli_job)


# Test Git secrets added
def test_git_secret_add_to_job(mcli_job: MCLIK8sJob):

    secret = SECRETS[SecretType.git]
    assert isinstance(secret, MCLIGitSSHSecret)
    secret.add_to_job(mcli_job)
    check_volume_and_mount(secret, mcli_job)

    # Check env vars
    env_spec = get_kube_spec(mcli_job.environment_variables)
    assert isinstance(env_spec, list)

    ev = env_spec[1]
    assert ev['name'] == 'GIT_SSH_COMMAND'
    assert ev['value'].endswith(f'{secret.mount_path}/secret')


# Test env secrets added
def test_env_secret_add_to_job(mcli_job: MCLIK8sJob):

    secret = SECRETS[SecretType.environment]
    assert isinstance(secret, MCLIEnvVarSecret)
    secret.add_to_job(mcli_job)

    # Check env value from
    env_spec = get_kube_spec(mcli_job.environment_variables)
    assert isinstance(env_spec, list)

    ev = env_spec[0]
    assert ev['name'] == secret.key
    assert ev['valueFrom']['secretKeyRef']['name'] == secret.name
    assert ev['valueFrom']['secretKeyRef']['key'] == 'value'


# Test OCI mounts were added
def test_oci_secret_add_to_job(mcli_job: MCLIK8sJob):
    secret = SECRETS[SecretType.oci]
    assert isinstance(secret, MCLIOCISecret)
    assert secret.mount_directory is not None
    secret.add_to_job(mcli_job)

    # Check volumes
    volumes_spec = get_kube_spec(mcli_job.pod_volumes)
    assert isinstance(volumes_spec, list)

    vol_spec = volumes_spec[0]
    assert vol_spec['name'] == secret.name
    assert vol_spec['secret']['secretName'] == secret.name

    secret_spec = vol_spec['secret']
    assert secret_spec['items'][0] == {'key': 'config', 'path': 'config'}
    assert secret_spec['items'][1] == {'key': 'key_file', 'path': 'key_file'}

    # Check mounts
    mounts_spec = get_kube_spec(mcli_job.container_volume_mounts)
    assert isinstance(mounts_spec, list)

    m = mounts_spec[0]
    assert m['name'] == secret.name
    assert m['mountPath'] == secret.mount_directory

    # Check env var
    env_spec = get_kube_spec(mcli_job.environment_variables)
    assert isinstance(env_spec, list)

    assert env_spec[0] == {'name': 'OCI_CONFIG_FILE', 'value': f'{secret.mount_directory}/config'}
    assert env_spec[1] == {'name': 'OCI_CLI_KEY_FILE', 'value': f'{secret.mount_directory}/key_file'}
    assert env_spec[2] == {'name': 'OCI_CLI_CONFIG_FILE', 'value': f'{secret.mount_directory}/config'}


# Test S3 mounts added
def test_s3_secret_add_to_job(mcli_job: MCLIK8sJob):

    secret = SECRETS[SecretType.s3]
    assert isinstance(secret, MCLIS3Secret)
    assert secret.mount_directory is not None
    secret.add_to_job(mcli_job)

    # Check volumes
    volumes_spec = get_kube_spec(mcli_job.pod_volumes)
    assert isinstance(volumes_spec, list)

    v = volumes_spec[0]
    assert v['name'] == secret.name
    assert v['secret']['secretName'] == secret.name
    assert v['secret']['items'][0] == {'key': 'credentials', 'path': 'credentials'}
    assert v['secret']['items'][1] == {'key': 'config', 'path': 'config'}

    # Check mounts
    mounts_spec = get_kube_spec(mcli_job.container_volume_mounts)
    assert isinstance(mounts_spec, list)

    m = mounts_spec[0]
    assert m['name'] == secret.name
    assert m['mountPath'] == secret.mount_directory

    # Check env var
    env_spec = get_kube_spec(mcli_job.environment_variables)
    assert isinstance(env_spec, list)

    assert env_spec[0] == {'name': 'AWS_CONFIG_FILE', 'value': f'{secret.mount_directory}/config'}
    assert env_spec[1] == {'name': 'AWS_SHARED_CREDENTIALS_FILE', 'value': f'{secret.mount_directory}/credentials'}


# Test GCP mounts added
def test_gcp_secret_add_to_job(mcli_job: MCLIK8sJob):

    secret = SECRETS[SecretType.gcp]
    assert isinstance(secret, MCLIGCPSecret)
    assert secret.mount_path is not None
    secret.add_to_job(mcli_job)
    check_volume_and_mount(secret, mcli_job)

    # Check env var
    env_spec = get_kube_spec(mcli_job.environment_variables)
    assert isinstance(env_spec, list)

    ev = env_spec[1]
    assert ev == {'name': 'GOOGLE_APPLICATION_CREDENTIALS', 'value': f'{secret.mount_path}/secret'}


# Test writing to and reading from Kubernetes specs
@pytest.mark.parametrize('secret', SECRETS.values())
def test_secret_write_read(secret: Secret):
    cluster_secret = ClusterSecret(secret)
    secret_spec = cluster_secret.to_kube_spec()
    imported_secret = ClusterSecret.from_kube_spec(secret_spec)
    assert asdict(cluster_secret.secret) == asdict(imported_secret.secret)
