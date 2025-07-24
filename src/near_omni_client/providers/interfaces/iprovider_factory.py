from abc import ABC, abstractmethod

from web3 import Web3

from near_omni_client.json_rpc.client import NearClient
from near_omni_client.networks.network import Network


class IProviderFactory(ABC):
    @abstractmethod
    def get_provider(self, network: Network) -> Web3 | NearClient:
        pass

    @abstractmethod
    def is_network_supported(self, network: Network) -> bool:
        pass
