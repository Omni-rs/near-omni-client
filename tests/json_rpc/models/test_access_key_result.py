from near_omni_client.json_rpc.models import AccessKeyResult


def test_access_key_result_parsing():
    sample = {
        "jsonrpc": "2.0",
        "result": {
            "block_hash": "J1zkrK8sHuzzV8pkXsEPrZH7SQZeJ2NSEs9L1hSWzVgg",
            "block_height": 187316844,
            "nonce": 187309654000001,
            "permission": {
                "FunctionCall": {
                    "allowance": "149788200694421800000000",
                    "method_names": [
                        "write_record",
                        "get_record",
                        "get_greeting",
                        "__contract_abi",
                        "contract_source_metadata",
                    ],
                    "receiver_id": "contract.rpc-examples.testnet",
                }
            },
        },
        "id": "dontcare",
    }

    result = AccessKeyResult.from_json_response(sample)
    assert result.permission.function_call.receiver_id == "contract.rpc-examples.testnet"
