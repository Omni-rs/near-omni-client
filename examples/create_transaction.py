import asyncio
from near_omni_client.transactions import TransactionBuilder, ActionFactory
from near_omni_client.signers import KeypairSigner
from near_omni_client.transactions import Transactions, TxExecutionStatus
from near_omni_client.json_rpc.providers import JsonRpcProvider

async def main():
    # 1) Create a transaction
    tx_builder = TransactionBuilder()
    tx = (
        tx_builder.with_signer_id("alice.testnet")
        .with_public_key(bytes.fromhex("…32 bytes…"))
        .with_nonce(42)
        .with_receiver("contract.testnet")
        .with_block_hash(bytes.fromhex("…32 bytes…"))
        .add_action(
            ActionFactory.function_call(
                "do_work",
                b'{"foo":"bar"}',
                gas=100_000_000_000_000,
                deposit=0,
            )
        )
        .build()
    )

    provider_url = "https://rpc.testnet.near.org"
    json_rpc_provider = JsonRpcProvider(provider_url)
    # provider = JsonRpcProvider(json_rpc_provider) 
    # 2) Sign the transaction
    # signer = KeypairSigner("ed25519:…private key…")
    # signed_b64 = signer.sign_base64(tx)

    # 3) Propagate the transaction
    # provider = HttpProvider("https://rpc.testnet.near.org")
    # tx_client = Transactions(provider)
    # result = await tx_client.send_transaction(
    #     signed_tx_base64=signed_b64,
    #     wait_until=TxExecutionStatus.INCLUDED_FINAL,
    # )

    # print("Hash:", result.transaction.hash)
    # print("Final status:", result.final_execution_status)


if __name__ == "__main__":
    asyncio.run(main())


# from near_omni_client.signers import MpcSigner
# from near_omni_client.wallets import NearWallet

# mpc = MpcContract(connection, contract_id)
# signer = MpcSigner(mpc)
# wallet = NearWallet(provider, signer)
# await wallet.send_some_transaction(...)
