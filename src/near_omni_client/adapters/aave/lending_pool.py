from web3 import Web3
from near_omni_client.networks import Network
from near_omni_client.wallets import Wallet


class LendingPool:
    # addresses obtained from https://aave.com/docs/resources/addresses
    contract_addresses = {
        Network.ETHEREUM_MAINNET: Web3.to_checksum_address(
            "0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2"
        ),  # https://github.com/bgd-labs/aave-address-book/blob/main/src/AaveV3Ethereum.sol
        Network.ETHEREUM_SEPOLIA: Web3.to_checksum_address(
            "0x6Ae43d3271ff6888e7Fc43Fd7321a503ff738951"
        ),  # https://github.com/bgd-labs/aave-address-book/blob/main/src/AaveV3Sepolia.sol
        Network.BASE_MAINNET: Web3.to_checksum_address(
            "0xA238Dd80C259a72e81d7e4664a9801593F98d1c5"
        ),  # https://github.com/bgd-labs/aave-address-book/blob/main/src/AaveV3Base.sol
        Network.BASE_SEPOLIA: Web3.to_checksum_address(
            "0x8bAB6d1b75f19e9eD9fCe8b9BD338844fF79aE27"
        ),  # https://github.com/bgd-labs/aave-address-book/blob/main/src/AaveV3BaseSepolia.sol
    }

    abi = [
        {
            "name": "supply",
            "type": "function",
            "inputs": [
                {"name": "asset", "type": "address"},
                {"name": "amount", "type": "uint256"},
                {"name": "onBehalfOf", "type": "address"},
                {"name": "referralCode", "type": "uint16"},
            ],
            "outputs": [],
            "stateMutability": "public",
            "constant": False,
            "virtual": True,
            "payable": False,
        },
        {
            "name": "withdraw",
            "type": "function",
            "inputs": [
                {"name": "asset", "type": "address"},
                {"name": "amount", "type": "uint256"},
                {"name": "to", "type": "address"},
            ],
            "outputs": [{"name": "", "type": "uint256"}],
            "stateMutability": "public",
            "constant": False,
            "virtual": True,
            "payable": False,
        },
    ]

    def __init__(self, network: Network, wallet: Wallet):
        self.network = network
        self.contract_address = self.contract_addresses.get(network)
        self.wallet = wallet

        if not self.contract_address:
            raise ValueError(f"Unsupported network: {network}")

        self.contract_address = Web3.to_checksum_address(self.contract_address)
        self.contract = Web3().eth.contract(None, abi=self.abi)  # No provider needed

    @staticmethod
    def get_address_for_network(network: Network) -> str:
        address = LendingPool.contract_addresses.get(network)
        if not address:
            raise ValueError(f"Unsupported network: {network}")
        return address

    def supply(
        self,
        asset_address: str,
        amount: int,
        on_behalf_of: str = None,
        referral_code: int = 0,
        gas_limit: int = 1000000,
        wait: bool = True,
    ) -> str:
        """
        Supply assets to the AAVE protocol.

        Args:
            asset_address: Address of the asset to supply
            amount: Amount to supply in base units
            on_behalf_of: Address that will receive the aTokens (defaults to sender)
            referral_code: Code used to register the integrator (0 if none)
            gas_limit: Maximum gas to use
            wait: Whether to wait for transaction confirmation
        """
        if on_behalf_of is None:
            on_behalf_of = self.wallet.get_address()

        tx = self.contract.functions.supply(
            asset_address, amount, on_behalf_of, referral_code
        ).build_transaction(
            {
                "from": self.wallet.get_address(),
                "to": self.contract_address,
                "gas": gas_limit,
                "nonce": self.wallet.get_nonce(self.network),
                "chainId": self.wallet.get_chain_id(self.network),
                "maxFeePerGas": Web3.to_wei(2, "gwei"),
                "maxPriorityFeePerGas": Web3.to_wei(1, "gwei"),
            }
        )

        return self.wallet.sign_and_send_transaction(self.network, tx, wait)

    def withdraw(
        self,
        asset_address: str,
        amount: int,
        to_address: str = None,
        gas_limit: int = 1000000,
        wait: bool = True,
    ) -> str:
        """
        Withdraw assets from the AAVE protocol.

        Args:
            asset_address: Address of the asset to withdraw
            amount: Amount to withdraw in base units
            to_address: Address that will receive the withdrawn assets (defaults to sender)
            gas_limit: Maximum gas to use
            wait: Whether to wait for transaction confirmation
        """
        if to_address is None:
            to_address = self.wallet.get_address()

        tx = self.contract.functions.withdraw(asset_address, amount, to_address).build_transaction(
            {
                "from": self.wallet.get_address(),
                "to": self.contract_address,
                "gas": gas_limit,
                "nonce": self.wallet.get_nonce(self.network),
                "chainId": self.wallet.get_chain_id(self.network),
                "maxFeePerGas": Web3.to_wei(2, "gwei"),
                "maxPriorityFeePerGas": Web3.to_wei(1, "gwei"),
            }
        )

        return self.wallet.sign_and_send_transaction(self.network, tx, wait)
