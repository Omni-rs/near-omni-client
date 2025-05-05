import pytest
from near_omni_client.json_rpc.access_keys import AccessKey
from near_omni_client.json_rpc.exceptions import UnknownBlockError,InvalidAccountError,UnknownAccountError, UnknownAccessKeyError, UnavailableShardError, NoSyncedBlocksError, ParseError, InternalError
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
async def test_view_access_key_raises_unknown_block():
    mock_response = {
        "jsonrpc": "2.0",
        "error": {
            "name": "HANDLER_ERROR",
            "cause": {"name": "UNKNOWN_BLOCK", "info": {}},
            "code": -32000,
            "data": "block not found",
            "message": "Server error",
        },
        "id": "dontcare",
    }

    client = AccessKey(provider=MockProvider(mock_response))

    with pytest.raises(UnknownBlockError) as exc_info:
        await client.view_access_key("account.testnet", "ed25519:fakeKey")

    assert isinstance(exc_info.value, UnknownBlockError)


@pytest.mark.asyncio
async def test_view_access_key_raises_invalid_account():
    mock_response = {
        "jsonrpc": "2.0",
        "error": {
            "name": "HANDLER_ERROR",
            "cause": {"name": "INVALID_ACCOUNT", "info": {}},
            "code": -32000,
            "data": "invalid account format",
            "message": "Server error",
        },
        "id": "dontcare",
    }

    client = AccessKey(provider=MockProvider(mock_response))

    with pytest.raises(InvalidAccountError) as exc_info:
        await client.view_access_key("invalid_account", "ed25519:fakeKey")

    assert isinstance(exc_info.value, InvalidAccountError)


@pytest.mark.asyncio
async def test_view_access_key_raises_unknown_account():
    mock_response = {
        "jsonrpc": "2.0",
        "error": {
            "name": "HANDLER_ERROR",
            "cause": {"name": "UNKNOWN_ACCOUNT", "info": {}},
            "code": -32000,
            "data": "account not found",
            "message": "Server error",
        },
        "id": "dontcare",
    }

    client = AccessKey(provider=MockProvider(mock_response))

    with pytest.raises(UnknownAccountError) as exc_info:
        await client.view_access_key("nonexistent.testnet", "ed25519:fakeKey")

    assert isinstance(exc_info.value, UnknownAccountError)


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


@pytest.mark.asyncio
async def test_view_access_key_raises_unavailable_shard():
    mock_response = {
        "jsonrpc": "2.0",
        "error": {
            "name": "HANDLER_ERROR",
            "cause": {"name": "UNAVAILABLE_SHARD", "info": {}},
            "code": -32000,
            "data": "shard not available",
            "message": "Server error",
        },
        "id": "dontcare",
    }

    client = AccessKey(provider=MockProvider(mock_response))

    with pytest.raises(UnavailableShardError) as exc_info:
        await client.view_access_key("account.testnet", "ed25519:fakeKey")

    assert isinstance(exc_info.value, UnavailableShardError)


@pytest.mark.asyncio
async def test_view_access_key_raises_no_synced_blocks():
    mock_response = {
        "jsonrpc": "2.0",
        "error": {
            "name": "HANDLER_ERROR",
            "cause": {"name": "NO_SYNCED_BLOCKS", "info": {}},
            "code": -32000,
            "data": "no synced blocks",
            "message": "Server error",
        },
        "id": "dontcare",
    }

    client = AccessKey(provider=MockProvider(mock_response))

    with pytest.raises(NoSyncedBlocksError) as exc_info:
        await client.view_access_key("account.testnet", "ed25519:fakeKey")

    assert isinstance(exc_info.value, NoSyncedBlocksError)


@pytest.mark.asyncio
async def test_view_access_key_raises_parse_error():
    mock_response = {
        "jsonrpc": "2.0",
        "error": {
            "name": "REQUEST_VALIDATION_ERROR",
            "cause": {"name": "PARSE_ERROR", "info": {}},
            "code": -32000,
            "data": "parse error",
            "message": "Server error",
        },
        "id": "dontcare",
    }

    client = AccessKey(provider=MockProvider(mock_response))

    with pytest.raises(ParseError) as exc_info:
        await client.view_access_key("account.testnet", "ed25519:fakeKey")

    assert isinstance(exc_info.value, ParseError)


@pytest.mark.asyncio
async def test_view_access_key_raises_internal_error():
    mock_response = {
        "jsonrpc": "2.0",
        "error": {
            "name": "INTERNAL_ERROR",
            "cause": {"name": "INTERNAL_ERROR", "info": {}},
            "code": -32000,
            "data": "internal server error",
            "message": "Server error",
        },
        "id": "dontcare",
    }

    client = AccessKey(provider=MockProvider(mock_response))

    with pytest.raises(InternalError) as exc_info:
        await client.view_access_key("account.testnet", "ed25519:fakeKey")

    assert isinstance(exc_info.value, InternalError)