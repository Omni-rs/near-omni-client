import pytest

from near_omni_client.json_rpc.models import AccountResult, CallFunctionResult
from near_omni_client.json_rpc.accounts import Accounts
from tests.json_rpc.mocks import MockProvider

# ------------------------------------------------------
# View Account
# ------------------------------------------------------
@pytest.mark.asyncio
async def test_view_account():
    account_id = "test.near"
    mock_response = {
        "jsonrpc": "2.0",
        "result": {
            "amount": "999788200694421800000000",
            "block_hash": "56xEo2LorUFVNbkFhCncFSWNiobdp1kzm14nZ47b5JVW",
            "block_height": 187440904,
            "code_hash": "11111111111111111111111111111111",
            "locked": "0",
            "storage_paid_at": 0,
            "storage_usage": 410
        },
        "id": "dontcare"
    }

    provider = MockProvider(mock_response)
    accounts = Accounts(provider)

    result = await accounts.view_account(account_id)

    assert isinstance(result, AccountResult)
    assert result.block_hash == "56xEo2LorUFVNbkFhCncFSWNiobdp1kzm14nZ47b5JVW"
    assert result.amount == "999788200694421800000000"

# ------------------------------------------------------
# Call Function
# ------------------------------------------------------
@pytest.mark.asyncio
async def test_call_function():
    method_name = "get_greeting"
    account_id = "test.near"
    mock_response = {
        "jsonrpc": "2.0",
        "result": {
            "block_hash": "GTZdXfNmnL6TkJFdBeVMHCadgLuKChVfRNCSVsEQoJ7L",
            "block_height": 187444191,
            "logs": [],
            "result": [
                34, 71, 114, 101, 101, 116, 105, 110, 103, 115, 32, 102, 114, 111, 109,
                32, 78, 69, 65, 82, 32, 80, 114, 111, 116, 111, 99, 111, 108, 33, 34
            ]
        },
        "id": "dontcare"
    }

    provider = MockProvider(mock_response)
    accounts = Accounts(provider)

    result = await accounts.call_function(account_id, method_name, {})

    assert isinstance(result, CallFunctionResult)
    assert result.decoded_result() == '"Greetings from NEAR Protocol!"'