from web3 import Web3

from near_omni_client.json_rpc.client import NearClient
from near_omni_client.networks.network import Network
from near_omni_client.providers.evm import AlchemyFactoryProvider
from near_omni_client.providers.evm.local_provider import LocalProvider
from near_omni_client.providers.near import NearFactoryProvider

from .interfaces.iprovider_factory import IProviderFactory


class FactoryProvider(IProviderFactory):
    def __init__(self):
        self.supported_networks = [
            Network.LOCALHOST,
            Network.NEAR_MAINNET,
            Network.NEAR_TESTNET,
            Network.BASE_MAINNET,
            Network.BASE_SEPOLIA,
            Network.ETHEREUM_MAINNET,
            Network.ETHEREUM_SEPOLIA,
        ]

    def get_provider(self, network: Network) -> Web3 | NearClient:
        if not isinstance(network, Network):
            raise TypeError(f"Expected Network enum, got {type(network)}")

        if network == Network.NEAR_TESTNET or network == Network.BASE_SEPOLIA:
            return NearFactoryProvider().get_provider(network)

        if network == Network.LOCALHOST:
            return LocalProvider().get_provider(network)

        if network in [
            Network.ETHEREUM_MAINNET,
            Network.ETHEREUM_SEPOLIA,
            Network.BASE_MAINNET,
            Network.BASE_SEPOLIA,
        ]:
            return AlchemyFactoryProvider().get_provider(network)

        raise ValueError(f"Unsupported network: {network.name}")

    def is_network_supported(self, network: Network) -> bool:
        return network in self.supported_networks
