"""Mix-in for creating PV and PVC on cluster setup"""
from abc import ABC, abstractmethod
from dataclasses import dataclass, fields
from typing import Dict, NamedTuple, Optional

from kubernetes import client

from mcli.models.mcli_cluster import Cluster
from mcli.serverside.clusters.cluster import ClusterSetupError
from mcli.utils.utils_kube import kube_call_idem


class NFSVolume(NamedTuple):
    """An NFS Volume
    """
    path: str
    server: str


class CSIVolume(NamedTuple):
    """A CSI Volume
    """
    driver: str
    volumeHandle: str


@dataclass
class PVDetails:
    """Details for peristent volume specs
    """
    nfs: Optional[NFSVolume] = None
    csi: Optional[CSIVolume] = None

    def __post_init__(self):
        specified = set()
        for f in fields(self):
            if getattr(self, f.name, None):
                specified.add(f.name)

        if len(specified) == 0:
            raise RuntimeError('Must specify at least 1 type of volume')
        if len(specified) > 1:
            raise RuntimeError(f'Only 1 type of PV can be specified. Got: {list(specified)}')

    def to_dict(self) -> Dict[str, Dict[str, str]]:
        """Returns a dictionary of volume details to add to a V1PersistentVolumeSpec
        """
        details: Dict[str, str]
        for f in fields(self):
            spec = getattr(self, f.name, None)
            if spec is not None:
                details = spec._asdict()
                return {f.name: details}
        raise RuntimeError('Must specify at least 1 type of volume')


class PVSetupMixin(ABC):
    """Mix-in to add PV and PVC setup
    """

    storage_capacity: str = '5Gi'

    @property
    @abstractmethod
    def pv_name(self) -> str:
        """Name of the PV
        """

    @property
    @abstractmethod
    def pvc_name(self) -> str:
        """Name of the PVC
        """

    @abstractmethod
    def get_volume_details(self) -> PVDetails:
        """Returns the details of the PV spec
        """

    def setup_pv(self, cluster: Cluster) -> bool:
        """Creates the user's PVC and PV for their personal workdisk

        Returns:
            True if PV and PVC were successfully created

        Raises:
            ClusterSetupError: Raised if pv or pvc creation failed
        """

        # Create PV
        pv_spec = client.V1PersistentVolumeSpec(capacity={'storage': self.storage_capacity},
                                                access_modes=['ReadWriteMany'],
                                                **self.get_volume_details().to_dict())
        volume = client.V1PersistentVolume(
            api_version='v1',
            kind='PersistentVolume',
            spec=pv_spec,
            metadata=client.V1ObjectMeta(name=self.pv_name),
        )

        # Create PVC
        pvc_spec = client.V1PersistentVolumeClaimSpec(
            access_modes=['ReadWriteMany'],
            resources={'requests': {
                'storage': self.storage_capacity
            }},
            storage_class_name='',
        )
        claim = client.V1PersistentVolumeClaim(
            api_version='v1',
            kind='PersistentVolumeClaim',
            spec=pvc_spec,
            metadata=client.V1ObjectMeta(name=self.pvc_name),
        )

        claim_ref = client.V1ObjectReference(api_version='v1',
                                             kind='PersistentVolumeClaim',
                                             name=self.pvc_name,
                                             namespace=cluster.namespace)
        pv_spec.claim_ref = claim_ref

        # Deploy to Kubernetes
        with Cluster.use(cluster):
            api = client.CoreV1Api()
            try:
                kube_call_idem(api.create_persistent_volume, body=volume)
                kube_call_idem(api.create_namespaced_persistent_volume_claim, namespace=cluster.namespace, body=claim)
            except client.ApiException as e:
                raise ClusterSetupError(e) from e

        return True
