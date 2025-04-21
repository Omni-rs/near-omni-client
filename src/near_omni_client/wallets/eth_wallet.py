from eth_account import Account
from network import Network
from provider import IProviderFactory
from web3 import Web3
from web3.exceptions import TimeExhausted

class Wallet:
    def __init__(self, private_key: str, provider_factory: IProviderFactory, supported_networks: list[Network]):
        self.private_key = private_key
        self.account = Account.from_key(private_key)
        self.provider_factory = provider_factory
        self.supported_networks = supported_networks

        unsupported = [n for n in self.supported_networks if not self.provider_factory.is_network_supported(n)]
        if unsupported:
            raise ValueError(f"Provider does not support the following networks: {[n.name for n in unsupported]}")

    def get_web3(self, network: Network) -> Web3:
        return self.provider_factory.get_provider(network)

    def get_wallet_address(self) -> str:
        return self.account.address

    def get_nonce(self, network: Network) -> int:
        return self.get_web3(network).eth.get_transaction_count(self.account.address)

    def send_transaction(self, network: Network, tx_data: dict, wait: bool = True, timeout: int = 300) -> str:
        web3 = self.get_web3(network)
        
        # Sign the transaction
        signed_tx = web3.eth.account.sign_transaction(tx_data, self.private_key)
        
        # Send the transaction
        tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
        print(f"Transaction sent: 0x{tx_hash.hex()}")

        # Wait for confirmation if requested
        if wait:
            try:
                receipt = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=timeout)
                if receipt.status == 1:
                    print(f"Transaction confirmed: 0x{tx_hash.hex()}")
                else:
                    raise RuntimeError(f"Transaction failed on-chain: 0x{tx_hash.hex()}")
            except TimeExhausted:
                raise TimeoutError(f"Transaction not confirmed within {timeout} seconds: 0x{tx_hash.hex()}")

        return tx_hash

    def get_transaction_receipt(self, network: Network, tx_hash: str):
        return self.get_web3(network).eth.waitForTransactionReceipt(tx_hash)

    def get_balance(self, network: Network, address: str = None) -> float:
        web3 = self.get_web3(network)
        addr = address or self.get_wallet_address()
        balance = web3.eth.get_balance(addr)
        return Web3.from_wei(balance, 'ether')

    def get_chain_id(self, network: Network) -> int:
        return self.get_web3(network).eth.chain_id
    
    def wait_for_receipt(self, network: Network, tx_hash: str, timeout: int = 300):
        try:
            receipt = self.get_web3(network).eth.wait_for_transaction_receipt(tx_hash, timeout=timeout)
            return receipt
        except TimeExhausted:
            raise TimeoutError(f"Transaction {tx_hash.hex()} was not confirmed after {timeout} seconds.")

