import asyncio
import base64
import os

from near_omni_client.transactions import TransactionBuilder, ActionFactory
from near_omni_client.json_rpc.client import NearClient
from near_omni_client.transactions.utils import decode_key
from dotenv import load_dotenv


async def main():
    load_dotenv()

    private_key_str = os.getenv("NEAR_PRIVATE_KEY")
    public_key_str = os.getenv("NEAR_PUBLIC_KEY")
    account_id = os.getenv("NEAR_ACCOUNT_ID")

    # 1) Create a transaction
    near_client = NearClient(provider_url="https://rpc.testnet.near.org")
    nonce_and_block_hash = await near_client.get_nonce_and_block_hash(account_id, public_key_str)

    print("nonce_and_block_hash", nonce_and_block_hash)

    tx_builder = TransactionBuilder()
    tx = (
        tx_builder.with_signer_id(account_id)
        .with_public_key(public_key_str)
        .with_nonce(nonce_and_block_hash["nonce"])
        .with_receiver("contract.testnet")
        .with_block_hash(nonce_and_block_hash["block_hash"])
        .add_action(
            ActionFactory.transfer(
                deposit=1,
            )
        )
        .build()
    )

    # 2) Sign the transaction
    private_key_bytes = decode_key(private_key_str)
    signed_tx = tx.to_vec(private_key_bytes)
    print("signed_tx", signed_tx)

    signed_tx_bytes = bytes(bytearray(signed_tx))
    signed_tx_base64 = base64.b64encode(signed_tx_bytes).decode("utf-8")
    print("signed_tx_base64", signed_tx_base64)

    # 3) Send the transaction
    result = await near_client.send_raw_transaction(signed_tx_base64)
    print("result", result)


if __name__ == "__main__":
    asyncio.run(main())
