import pytest
from near_omni_client.json_rpc.access_key import AccessKeyClient
from near_omni_client.interfaces.provider import IJsonRpcProvider

class MockProvider(IJsonRpcProvider):
    async def call(self, method: str, params: dict):
        assert method == "query"
        assert params["request_type"] == "view_access_key"
        return {
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
                        "contract_source_metadata"
                    ],
                    "receiver_id": "contract.rpc-examples.testnet"
                }
            }
        }

@pytest.mark.asyncio
async def test_view_access_key():
    client = AccessKeyClient(provider=MockProvider())
    res = await client.view_access_key("account.rpc-examples.testnet", "ed25519:EddTahJwZpJjYPPmat7DBm1m2vdrFBzVv7e3T4hzkENd")
    assert res["nonce"] == 187309654000001
    assert res["permission"]["FunctionCall"]["receiver_id"] == "contract.rpc-examples.testnet"
