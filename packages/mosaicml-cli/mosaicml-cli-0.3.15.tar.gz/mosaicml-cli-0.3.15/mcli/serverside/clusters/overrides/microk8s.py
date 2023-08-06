""" Microk8s Cluster Definition """
from mcli.serverside.clusters.cluster import GenericK8sCluster
from mcli.serverside.clusters.cluster_instances import Instances, LocalInstances
from mcli.serverside.clusters.gpu_type import GPUType
from mcli.serverside.clusters.instance_type import InstanceType

MICROK8S_INSTANCES = LocalInstances(instance_types=[InstanceType(
    gpu_type=GPUType.NONE,
    gpu_num=0,
)])


class Microk8sCluster(GenericK8sCluster):
    """ Microk8s Cluster Overrides """
    allowed_instances: Instances = MICROK8S_INSTANCES
