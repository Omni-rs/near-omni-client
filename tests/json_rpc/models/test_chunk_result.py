from near_omni_client.json_rpc.models import ChunkResult


def test_chunk_result_model_parsing():
    sample = {
        "jsonrpc": "2.0",
        "result": {
            "author": "kiln.pool.f863973.m0",
            "header": {
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
            "receipts": [],
            "transactions": [
                {
                    "actions": [
                        {
                            "FunctionCall": {
                                "args": "eyJyZWNvcmRfaWQiOjEsInJlY29yZCI6IkhlbGxvLCBOZWFyIFByb3RvY29sISJ9",
                                "deposit": "0",
                                "gas": 50000000000000,
                                "method_name": "write_record",
                            }
                        }
                    ],
                    "hash": "J3KbUXF9YPu2eGnbDCACxGvmMDZMdP7acGYhVLHGu9y2",
                    "nonce": 187309654000001,
                    "priority_fee": 0,
                    "public_key": "ed25519:EddTahJwZpJjYPPmat7DBm1m2vdrFBzVv7e3T4hzkENd",
                    "receiver_id": "contract.rpc-examples.testnet",
                    "signature": "ed25519:3opUQgg5eNQmE2LJ8zJiitBAVLDFR3svk8LC5VtVGorQuq8jWLocKAt7B4xb6n7DhH8zSVCWcRRrmVL9f1wHiVXa",
                    "signer_id": "account.rpc-examples.testnet",
                }
            ],
        },
        "id": "dontcare",
    }

    result = ChunkResult.from_json_response(sample)

    # author & header
    assert result.author == "kiln.pool.f863973.m0"
    hdr = result.header
    assert hdr.chunk_hash == "CzPafxtJmM1FnRoasKWAVhceJzZzkz9RKUBQQ4kY9V1v"
    assert hdr.shard_id == 0
    assert hdr.bandwidth_requests is None  # null → None
    assert hdr.balance_burnt == "0"

    # receipts
    assert result.receipts == []

    # transactions
    txs = result.transactions
    assert len(txs) == 1
    tx = txs[0]
    assert tx.hash == "J3KbUXF9YPu2eGnbDCACxGvmMDZMdP7acGYhVLHGu9y2"
    action = tx.actions[0]
    fc = action.function_call
    assert fc.method_name == "write_record"
    assert fc.deposit == "0"
    assert fc.gas == 50000000000000
