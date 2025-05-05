from near_omni_client.json_rpc.models import AccessKeyListResult


def test_access_keys_list_result_parsing():
    sample = {
        "jsonrpc": "2.0",
        "result": {
            "block_hash": "29G6xeV4ufkVsY24YZPfiRwLMTNoKrAMitrjg6nvVZqq",
            "block_height": 187319080,
            "keys": [
                {
                    "access_key": {
                        "nonce": 187309654000000,
                        "permission": "FullAccess"
                    },
                    "public_key": "ed25519:vJBU18AtvePANmepMoY3rtV3wt1RHwqoktak82E4d2M"
                },
                {
                    "access_key": {
                        "nonce": 187309654000001,
                        "permission": {
                            "FunctionCall": {
                                "allowance": "149788200694421800000000",
                                "method_names": [
                                    "write_record",
                                    "get_record",
                                    "get_greeting",
                                    "__contract_abi",
                                    "contract_source_metadata"
                                ],
                                "receiver_id": "contract.rpc-examples.testnet"
                            }
                        }
                    },
                    "public_key": "ed25519:EddTahJwZpJjYPPmat7DBm1m2vdrFBzVv7e3T4hzkENd"
                }
            ]
        },
        "id": "dontcare"
    }

    result = AccessKeyListResult.from_json_response(sample)

    assert result.block_hash == "29G6xeV4ufkVsY24YZPfiRwLMTNoKrAMitrjg6nvVZqq"
    assert result.block_height == 187319080
    assert len(result.keys) == 2

    first_key = result.keys[0]
    assert first_key.public_key == "ed25519:vJBU18AtvePANmepMoY3rtV3wt1RHwqoktak82E4d2M"
    assert first_key.access_key.nonce == 187309654000000
    assert first_key.access_key.permission.full_access is not None
    assert first_key.access_key.permission.function_call is None

    second_key = result.keys[1]
    assert second_key.public_key == "ed25519:EddTahJwZpJjYPPmat7DBm1m2vdrFBzVv7e3T4hzkENd"
    assert second_key.access_key.nonce == 187309654000001
    assert second_key.access_key.permission.full_access is None
    assert second_key.access_key.permission.function_call is not None
    assert second_key.access_key.permission.function_call.receiver_id == "contract.rpc-examples.testnet"
