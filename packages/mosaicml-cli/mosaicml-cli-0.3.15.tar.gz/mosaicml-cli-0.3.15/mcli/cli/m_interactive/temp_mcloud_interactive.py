"""
This implements interactive for clusters with exec privileges by submitting sleeper jobs to
MCloud. It is a temporary solution until the cloud version of interactive is built and therefore
purposely avoids messing with the mcli config or kube config like legacy kube mcli. It should be
removed when interactive is supported in MCloud
"""
import logging
import shlex
import subprocess
from typing import Any, Dict, Optional, cast

from kubernetes import config as kube_config

from mcli.config import MCLIConfig
from mcli.sdk import Run, RunConfig, RunStatus, create_run, get_clusters, get_runs, wait_for_run_status
from mcli.utils.utils_interactive import simple_prompt
from mcli.utils.utils_logging import INFO, OK, WARN

logger = logging.getLogger(__name__)


# pylint: disable=too-many-statements
def mcloud_interactive(
    name: Optional[str] = None,
    cluster: Optional[str] = None,
    gpu_type: Optional[str] = None,
    gpus: Optional[int] = None,
    cpus: int = 1,
    hours: Optional[float] = None,
    image: str = 'mosaicml/pytorch',
    rank: int = 0,
    connect: bool = True,
    reconnect: Optional[str] = None,
) -> int:

    run: Optional[Run] = None

    if reconnect:
        all_runs = get_runs([reconnect], include_details=True)
        if not all_runs:
            raise RuntimeError(f'Could not find an interactive session named {reconnect}')

        run = all_runs[0]
        if run.status >= RunStatus.TERMINATING:
            raise RuntimeError(f'Run {run.name} is {run.status.value}. Please select a running run')
        cluster = run.config.cluster
        logger.info(f'{INFO} Attempting to reconnect to session: [cyan]{run.name}[/]')
    elif reconnect is not None:
        raise RuntimeError('Reconnect argument `-r` requires a run name')

    if not cluster:
        clusters = get_clusters()
        if not clusters:
            raise RuntimeError('Cluster name must be provided. Use `mcli get clusters` to list available clusters')
        elif len(clusters) == 1:
            cluster = clusters[0].name
        else:
            raise RuntimeError('Multiple clusters available. Please use the --cluster argument to set the '
                               'cluster to use for interactive')

    if not reconnect:
        if cpus and cpus != 1:
            logger.info(f'{WARN} Specifying cpus not currently supported. Submitting interactive run with {gpus} gpus')

        config = RunConfig(
            name=name or f'interactive-{(gpu_type or "none").replace("_", "-")}-{gpus or 0}'.lower(),
            image=image,
            command=f'sleep {int(3600 * (hours or 1))}',
            gpu_num=gpus,
            gpu_type=gpu_type,
            cluster=cluster,
            optimization_level=0,
        )

        run = create_run(config)
        logger.info(f'{OK} Interactive session [cyan]{run.name}[/] submitted')

    assert run  # run is set in reconnect/not reconnect blocks

    if connect:
        context = simple_prompt(
            f'Which kube context should be used to connect to the interactive run? [{cluster}]',
            default=cluster,
            mandatory=False,
        )

        kube_config.load_kube_config()

        default_namespace = ''
        for c in kube_config.list_kube_config_contexts()[0]:
            c = cast(Dict[str, Any], c)
            if c.get('name') == context:
                default_namespace = c.get('context', {}).get('namespace', '')
                break

        if MCLIConfig.load_config(safe=True).internal:
            default_namespace = 'mosaicml-orchestration'

        namespace = simple_prompt(
            f'Which kube namespace should be used to connect to the interactive run? [{default_namespace}]',
            default=default_namespace,
            mandatory=False,
        )

        pod_id = f"{run.last_attempt_id}-{rank}"
        logger.info(f'{INFO} Waiting for session to start with pod [blue]{pod_id}[/]...')
        logger.info(f'{INFO} Press Ctrl+C to quit and interact with your session manually.')
        run = wait_for_run_status(run, status=RunStatus.RUNNING, timeout=300)

        rank_str = f"node rank [cyan]{rank}[/] of " if rank > 0 else ""
        logger.info(f'{OK} Connecting to {rank_str}interactive session [cyan]{run.name}[/]')

        options = []
        if context:
            options.append(f'--context {shlex.quote(context)}')
        if namespace:
            options.append(f'--namespace {shlex.quote(namespace)}')

        exec_command = f'kubectl exec -it {" ".join(options)} {pod_id} -c main -- /bin/bash'

        with subprocess.Popen(exec_command, shell=True, start_new_session=True) as p:
            return p.wait() == 0

    return 0
