from .eth_wallet import EthereumWallet
from .near_wallet import NearWallet
from .interfaces.wallet import Wallet

__all__ = ["EthereumWallet", "NearWallet", "Wallet"]
