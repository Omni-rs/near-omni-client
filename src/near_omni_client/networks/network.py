from enum import Enum

BASE_DOMAIN = "6"
ETHEREUM_DOMAIN = "0"


class Network(Enum):
    LOCALHOST = "localhost"
    BASE_SEPOLIA = "base-sepolia"
    BASE_MAINNET = "base-mainnet"
    ETHEREUM_SEPOLIA = "eth-sepolia"
    ETHEREUM_MAINNET = "eth-mainnet"
    NEAR_MAINNET = "near-mainnet"
    NEAR_TESTNET = "near-testnet"

    @staticmethod
    def parse(value: str) -> "Network":
        try:
            return Network(value)
        except KeyError:
            raise ValueError(f"Invalid network value: {value}")

    @property
    def domain(self) -> str:
        if self in {Network.BASE_SEPOLIA, Network.BASE_MAINNET}:
            return BASE_DOMAIN
        elif self in {Network.ETHEREUM_SEPOLIA, Network.ETHEREUM_MAINNET}:
            return ETHEREUM_DOMAIN
        else:
            raise ValueError(f"Unknown domain for network {self}")
