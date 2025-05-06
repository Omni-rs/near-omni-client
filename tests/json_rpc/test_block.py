# tests/json_rpc/test_block.py

import pytest
from near_omni_client.json_rpc.block import Block
from near_omni_client.json_rpc.models import BlockResult
from tests.json_rpc.mocks import MockProvider

mock_block_response = {
    "jsonrpc": "2.0",
    "result": {
        "author": "node2",
        "chunks": [
            {
                "balance_burnt": "0",
                "bandwidth_requests": None,
                "chunk_hash": "CzPafxtJmM1FnRoasKWAVhceJzZzkz9RKUBQQ4kY9V1v",
                "congestion_info": {
                    "allowed_shard": 1,
                    "buffered_receipts_gas": "0",
                    "delayed_receipts_gas": "0",
                    "receipt_bytes": 0,
                },
                "encoded_length": 308,
                "encoded_merkle_root": "6z9JwwtVfS5nRKcKeJxgzThRRs2wCNvbH88T3cuARe6W",
                "gas_limit": 1000000000000000,
                "gas_used": 0,
                "height_created": 187310138,
                "height_included": 187310138,
                "outcome_root": "11111111111111111111111111111111",
                "outgoing_receipts_root": "AChfy3dXeJjgD2w5zXkUTFb6w8kg3AYGnyyjsvc7hXLv",
                "prev_block_hash": "Wj6B3RTv73EWDNbSammRDeA9315RaPyRrJYmiP4nG4X",
                "prev_state_root": "cRMk2zd2bWC1oBfGowgMTpqW9L5SNG2FeE72yT1wpQA",
                "rent_paid": "0",
                "shard_id": 0,
                "signature": "ed25519:L1iCopW8gY5rqwfuZT8Y3bHHXvuvWT87X9rwdY6LmFi8LGZdMhj2CkQCXLGrzdfYXD8B54wPTM9TqJAHcKfFDyW",
                "tx_root": "CMwUsP8q4DTBUYxXm12jVwC8xTD8L1T1n3jdKLQVh6bm",
                "validator_proposals": [],
                "validator_reward": "0",
            },
            {
                "balance_burnt": "0",
                "bandwidth_requests": None,
                "chunk_hash": "44MZBWmPgXszAyojsffzozvNEdRsJcsq7RrdAV4Y7CLm",
                "congestion_info": {
                    "allowed_shard": 2,
                    "buffered_receipts_gas": "0",
                    "delayed_receipts_gas": "0",
                    "receipt_bytes": 0,
                },
                "encoded_length": 8,
                "encoded_merkle_root": "5TxYudsfZd2FZoMyJEZAP19ASov2ZD43N8ZWv8mKzWgx",
                "gas_limit": 1000000000000000,
                "gas_used": 0,
                "height_created": 187310138,
                "height_included": 187310138,
                "outcome_root": "11111111111111111111111111111111",
                "outgoing_receipts_root": "AChfy3dXeJjgD2w5zXkUTFb6w8kg3AYGnyyjsvc7hXLv",
                "prev_block_hash": "Wj6B3RTv73EWDNbSammRDeA9315RaPyRrJYmiP4nG4X",
                "prev_state_root": "EQ5mcUAzJA4du33f9g9YzKvdte2ukyRHMMHbbqdazZvU",
                "rent_paid": "0",
                "shard_id": 1,
                "signature": "ed25519:4ktZTtEfxXSXPVj6Kii52d2T684HKKtEMzrd3dNc7UyxmgkKcLtxD1fawtbj8KsmjbZPGj8YMzanDeViEhxRJtDX",
                "tx_root": "11111111111111111111111111111111",
                "validator_proposals": [],
                "validator_reward": "0",
            },
            # ...you can include more chunks if desired...
        ],
        "header": {
            "approvals": [
                None,
                "ed25519:5GhoQTPXsWpgGPq2ZHZCfP9iY9GSmHMNsnydzxBxnibGvC43PFUAD58aUSNyfepRY4dAMbjbf8CduMyQU83HBxAt",
            ],
            "block_body_hash": "6oSbpNUWcAUuaKWx79qTwyRPDLukg9hZ1RCa2PS5rcGt",
            "block_merkle_root": "DWK6gpunDXHgxU1KJi3Dx8o2HcKqQmUQJEaisK4M3ovD",
            "block_ordinal": 139413603,
            "challenges_result": [],
            "challenges_root": "11111111111111111111111111111111",
            "chunk_endorsements": [
                [255, 255],
                [251, 127],
            ],
            "chunk_headers_root": "4MjChqi5JChDhaiU4zkhN1jeygZiMd66KeHe3Gz9Vs7s",
            "chunk_mask": [True, True, True, True, True, True],
            "chunk_receipts_root": "7nEtD9XsDbRJy7MwvUg4QX5zDUktiEVRP9nM6hHpsHmX",
            "chunk_tx_root": "44YKYmcG1JTocmPSMGpriLwC8xTD8L1T1n3jdKLQVh6bm",
            "chunks_included": 6,
            "epoch_id": "HkFsp3sn9K3KDWVoWPCfUSQocgf5bH4icgjHijePc2aX",
            "epoch_sync_data_hash": None,
            "gas_price": "100000000",
            "hash": "6RWmTYhXCzjMjoY3Mz1rfFcnBm8E6XeDDbFEPUA4sv1w",
            "height": 187310138,
            "last_ds_final_block": "Wj6B3RTv73EWDNbSammRDeA9315RaPyRrJYmiP4nG4X",
            "last_final_block": "71qgTQCVFfjQkimSdnhxR8iWSP6o9jqumLcZ9k5g25mT",
            "latest_protocol_version": 73,
            "next_bp_hash": "AWcwcDPWUjcW9zGiAt7UEUZzZ5Ue77537turbvBLbsiB",
            "next_epoch_id": "FQBXgdi9oWKanYBXPP1sNUD93KMquocjT5mVrjQ4PH7E",
            "outcome_root": "7Qkowo41AoiMdNfyiT83DwvwyReMeqhrkpqTzGm4Z19T",
            "prev_hash": "Wj6B3RTv73EWDNbSammRDeA9315RaPyRrJYmiP4nG4X",
            "prev_height": 187310137,
            "prev_state_root": "AiApSbMNq9kPPEiLLWhFpSrX5HoPToaBXztM9fePX2ap",
            "random_value": "Br6a6tgEhNBZm9iPtxCLhwqwCr2eoEAGGMeVYZnU6fVF",
            "rent_paid": "0",
            "signature": "ed25519:YSuWifP5B3VBPuEVJppWt13AShXsWZ64Qus8uHmtddE2mY6u4jnZVv6Gz4tFvWXfBAkZDk5xtd95rUterEdQm5t",
            "timestamp": 1739254177539033760,
            "timestamp_nanosec": "1739254177539033760",
            "total_supply": "2515615267787707740507051994761921",
            "validator_proposals": [],
            "validator_reward": "0",
        },
    },
    "id": "dontcare",
}


@pytest.mark.asyncio
async def test_view_block_by_finality():
    provider = MockProvider(mock_block_response)
    blocks = Block(provider)

    result = await blocks.view_block(finality="final")

    assert isinstance(result, BlockResult)
    assert result.author == "node2"
    # header.hash comes from "hash" in the JSON header
    assert result.header.hash == "6RWmTYhXCzjMjoY3Mz1rfFcnBm8E6XeDDbFEPUA4sv1w"
    # first chunk gas_used is 0 in the sample
    assert result.chunks[0].gas_used == 0


@pytest.mark.asyncio
async def test_view_block_by_height():
    provider = MockProvider(mock_block_response)
    blocks = Block(provider)

    result = await blocks.view_block(block_id=187310138)

    assert isinstance(result, BlockResult)
    assert result.header.height == 187310138
    assert result.chunks[0].shard_id == 0


@pytest.mark.asyncio
async def test_view_block_by_hash():
    provider = MockProvider(mock_block_response)
    blocks = Block(provider)

    # use the actual block hash from the sample
    block_hash = mock_block_response["result"]["header"]["hash"]
    result = await blocks.view_block(block_id=block_hash)

    assert isinstance(result, BlockResult)
    assert result.header.hash == block_hash
    assert result.chunks[0].chunk_hash == "CzPafxtJmM1FnRoasKWAVhceJzZzkz9RKUBQQ4kY9V1v"
