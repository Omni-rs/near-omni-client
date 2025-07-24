import os

import pytest

from near_omni_client.adapters.aave import LendingPool
from near_omni_client.networks import Network
from near_omni_client.providers import FactoryProvider
from near_omni_client.wallets import EthereumWallet


@pytest.mark.skip(reason="Ignored while Anvil Fork is Available in the CI")
def test_aave_interest_rate_eth_mainnet():
    private_key = os.getenv("ETH_PRIVATE_KEY", "0xYOUR_PRIVATE_KEY_HERE")
    provider = FactoryProvider()
    wallet = EthereumWallet(
        private_key, provider_factory=provider, supported_networks=[Network.LOCALHOST]
    )
    adapter = LendingPool(Network.LOCALHOST, wallet)

    # USDC mainnet address
    usdc = "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"
    rate = adapter.get_interest_rate(usdc)

    slope = adapter.get_slope(usdc)
    print(f"USDC slope: {slope:.6f}")
    print(f"USDC currentLiquidityRate: {rate:.6f}%")
