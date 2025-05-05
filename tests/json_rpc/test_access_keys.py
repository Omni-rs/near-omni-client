import pytest
from near_omni_client.json_rpc.access_keys import AccessKey
from near_omni_client.json_rpc.exceptions import UnknownAccessKeyError
from tests.json_rpc.mocks import MockProvider


@pytest.mark.asyncio
async def test_view_access_key_function_call():
    mock_response = {
        "jsonrpc": "2.0",
        "result": {
            "block_hash": "J1zkrK8...",
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

    access_key_service = AccessKey(provider=MockProvider(mock_response))
    res = await access_key_service.view_access_key("account.testnet", "ed25519:abc123")

    assert res.nonce == 187309654000001
    assert res.permission.function_call is not None
    assert res.permission.function_call.receiver_id == "contract.rpc-examples.testnet"
    assert res.permission.full_access is None


@pytest.mark.asyncio
async def test_view_access_key_full_access():
    mock_response = {
        "jsonrpc": "2.0",
        "result": {
            "block_hash": "block123",
            "block_height": 123456789,
            "nonce": 42,
            "permission": {"FullAccess": {}},
        },
        "id": "dontcare",
    }

    client = AccessKey(provider=MockProvider(mock_response))
    res = await client.view_access_key("account.testnet", "ed25519:abc123")
    assert res.nonce == 42
    assert res.permission.full_access is not None
    assert res.permission.function_call is None


@pytest.mark.asyncio
async def test_view_access_key_raises_unknown_access_key():
    mock_response = {
        "jsonrpc": "2.0",
        "error": {
            "name": "HANDLER_ERROR",
            "cause": {"name": "UNKNOWN_ACCESS_KEY", "info": {}},
            "code": -32000,
            "data": "access key not found",
            "message": "Server error",
        },
        "id": "dontcare",
    }

    client = AccessKey(provider=MockProvider(mock_response))

    with pytest.raises(UnknownAccessKeyError) as exc_info:
        await client.view_access_key("nonexistent.testnet", "ed25519:fakeKey")

    assert isinstance(exc_info.value, UnknownAccessKeyError)
