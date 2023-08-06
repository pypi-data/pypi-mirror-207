""" Typing for Resource Requirements """
from __future__ import annotations

from typing import Dict, Union

from kubernetes import client

from mcli.utils.utils_kube_labels import label

SAFETY_MARGIN_CPU: float = 2
SAFETY_MARGIN_MEMORY: float = 0.1
SAFETY_MARGIN_STORAGE: float = 0.1


class MCLIK8sResourceRequirements(client.V1ResourceRequirements):
    """ Provides typing for Lazy Loaded V1ResourceRequirements

    Makes properties and nested properties lazy loaded for convenience
    """

    @classmethod
    def from_simple_resources(cls,
                              cpus: int,
                              memory: int,
                              storage: int,
                              include_margin: bool = True) -> MCLIK8sResourceRequirements:
        """Set resource requirements based on the provided values

        Args:
            cpus: Number of CPU cores
            memory: Memory in GB
            storage: Ephemeral storage in GB
            include_margin: Whether or not to use a safety margin. Defaults to True.

        Returns:
            MCLIK8sResourceRequirements
        """
        c = cls()
        if include_margin:
            c.cpus = cpus - SAFETY_MARGIN_CPU
            c.limit_cpus = cpus
            c.memory = memory * (1 - SAFETY_MARGIN_MEMORY)
            c.ephemeral_storage = storage * (1 - SAFETY_MARGIN_STORAGE)
        else:
            c.cpus = cpus
            c.memory = memory
            c.ephemeral_storage = storage

        return c

    @property
    def requests(self) -> Dict[str, str]:
        if self._requests is None:
            self._requests = {}
        return self._requests

    @requests.setter
    def requests(self, requests: Dict[str, str]):
        self._requests = requests

    @property
    def limits(self) -> Dict[str, str]:
        if self._limits is None:
            self._limits = {}
        return self._limits

    @limits.setter
    def limits(self, limits: Dict[str, str]):
        self._limits = limits

    @property
    def cpus(self) -> float:
        cpus_str = self.requests.get('cpu', '')
        try:
            if 'm' in cpus_str:
                return float(cpus_str.replace('m', '')) / 1000.0
            else:
                return float(cpus_str)
        except (TypeError, ValueError):
            pass
        return 0

    @cpus.setter
    def cpus(self, cpus: Union[str, float]):

        if isinstance(cpus, (float, int)):
            cpus_str = str(cpus)
        else:
            cpus_str = cpus
        self.requests['cpu'] = cpus_str
        self.limits['cpu'] = cpus_str

    @property
    def request_cpus(self):
        return self.cpus

    @request_cpus.setter
    def request_cpus(self, cpus: Union[str, float]):
        if isinstance(cpus, (float, int)):
            cpus_str = str(cpus)
        else:
            cpus_str = cpus
        self.requests['cpu'] = cpus_str

    @property
    def limit_cpus(self) -> float:
        cpus_str = self.limits.get('cpu', '')
        try:
            if 'm' in cpus_str:
                return float(cpus_str.replace('m', '')) / 1000.0
            else:
                return float(cpus_str)
        except (TypeError, ValueError):
            pass
        return 0

    @limit_cpus.setter
    def limit_cpus(self, cpus: Union[str, float]):
        if isinstance(cpus, (float, int)):
            cpus_str = str(cpus)
        else:
            cpus_str = cpus
        self.limits['cpu'] = cpus_str

    @property
    def gpus(self) -> int:
        gpus = self.requests.get(label.nvidia.GPU, 0)
        if isinstance(gpus, str):
            try:
                return int(gpus)
            except Exception as e:  #pylint: disable=broad-except
                raise ValueError(f'Non numeric GPU request set: {gpus}') from e
        return gpus

    @gpus.setter
    def gpus(self, gpus: int):
        self.requests[label.nvidia.GPU] = str(gpus)
        self.limits[label.nvidia.GPU] = str(gpus)

    @property
    def memory(self) -> float:
        """ Memory is received in GB """
        memory_str = self.requests.get('memory', '')
        try:
            if 'Gi' in memory_str:
                return float(memory_str.replace('Gi', '')) * 1024.0 / 1000.0
            elif 'G' in memory_str:
                return float(memory_str.replace('G', ''))
            elif 'Mi' in memory_str:
                return float(memory_str.replace('Mi', '')) * 1024.0 / 1000.0 / 1000.0
            elif 'M' in memory_str:
                return float(memory_str.replace('M', '')) / 1000.0

            # TODO: Stop being lazy and convert all possible valid formats
            print('WARNING: Possible Resource Memory Conversion Issue')

        except Exception:  # pylint: disable=broad-except
            pass
        return 0

    @memory.setter
    def memory(self, memory: Union[str, float]):
        """ Memory is set in GB """
        if isinstance(memory, (float, int)):
            memory_str = str(memory) + 'G'
        else:
            memory_str = memory
        self.requests['memory'] = memory_str
        self.limits['memory'] = memory_str

    @property
    def request_memory(self) -> float:
        return self.memory

    @request_memory.setter
    def request_memory(self, memory: Union[str, float]):
        """ Memory is set in GB """
        if isinstance(memory, (float, int)):
            memory_str = str(memory) + 'G'
        else:
            memory_str = memory
        self.requests['memory'] = memory_str

    @property
    def ephemeral_storage(self) -> float:
        """ Ephemeral Storage is received in GB """
        storage_str = self.requests.get('ephemeral-storage', '')
        try:
            if 'Gi' in storage_str:
                return float(storage_str.replace('Gi', '')) * 1024.0 / 1000.0
            elif 'G' in storage_str:
                return float(storage_str.replace('G', ''))
            elif 'Mi' in storage_str:
                return float(storage_str.replace('Mi', '')) * 1024.0 / 1000.0 / 1000.0
            elif 'M' in storage_str:
                return float(storage_str.replace('M', '')) / 1000.0

            # TODO: Stop being lazy and convert all possible valid formats
            print('WARNING: Possible Resource Ephermeral Storage Conversion Issue')

        except Exception:  # pylint: disable=broad-except
            pass
        return 0

    @ephemeral_storage.setter
    def ephemeral_storage(self, storage: Union[str, float]):
        """ Ephemeral Storage is set in GB """
        if isinstance(storage, (float, int)):
            storage_str = str(storage) + 'G'
        else:
            storage_str = storage
        self.requests['ephemeral-storage'] = storage_str
        self.limits['ephemeral-storage'] = storage_str

    @property
    def request_ephemeral_storage(self) -> float:
        return self.ephemeral_storage

    @request_ephemeral_storage.setter
    def request_ephemeral_storage(self, storage: Union[str, float]):
        """ Memory is set in GB """
        if isinstance(storage, (float, int)):
            storage_str = str(storage) + 'G'
        else:
            storage_str = storage
        self.requests['ephemeral-storage'] = storage_str

    @property
    def rdma_roce(self) -> int:
        rdma_roce_str = self.requests.get('rdma/roce', '0')
        return int(rdma_roce_str)

    @rdma_roce.setter
    def rdma_roce(self, rdma_roce: int):
        self.requests['rdma/roce'] = str(rdma_roce)
        self.limits['rdma/roce'] = str(rdma_roce)
