"""Primary import target for the Python API"""

# pyright: reportUnusedImport=false
# pylint: disable=useless-import-alias, disable=reimported

from mcli.api.cluster import get_clusters
from mcli.api.exceptions import MAPIException
from mcli.api.inference_deployments import (InferenceDeployment, InferenceDeploymentConfig, create_inference_deployment,
                                            delete_inference_deployments, get_inference_deployment_logs,
                                            get_inference_deployments, ping_inference_deployment, predict)
from mcli.api.runs import (FinalRunConfig, Run, RunConfig, RunStatus, create_run, delete_run, delete_runs,
                           follow_run_logs, get_run, get_run_logs, get_runs, start_run, start_runs, stop_run, stop_runs,
                           update_run_metadata, wait_for_run_status, watch_run_status)
from mcli.api.secrets import create_secret, delete_secrets, get_secrets
from mcli.cli.m_init.m_init import initialize
from mcli.cli.m_set_unset.api_key import set_api_key
from mcli.config import FeatureFlag, MCLIConfig

if not MCLIConfig.load_config(safe=True).feature_enabled(FeatureFlag.USE_MCLOUD):
    from mcli.api.kube.runs import (create_run, delete_runs, follow_run_logs, get_run_logs, get_runs, stop_runs,
                                    wait_for_run_status)
