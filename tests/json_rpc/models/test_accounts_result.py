from near_omni_client.json_rpc.models import AccountResult, CallFunctionResult


def test_account_result_parsing():
    sample = {
        "jsonrpc": "2.0",
        "result": {
            "amount": "999788200694421800000000",
            "block_hash": "56xEo2LorUFVNbkFhCncFSWNiobdp1kzm14nZ47b5JVW",
            "block_height": 187440904,
            "code_hash": "11111111111111111111111111111111",
            "locked": "0",
            "storage_paid_at": 0,
            "storage_usage": 410,
        },
        "id": "dontcare",
    }

    result = AccountResult.from_json_response(sample)

    assert result.amount == "999788200694421800000000"
    assert result.block_hash == "56xEo2LorUFVNbkFhCncFSWNiobdp1kzm14nZ47b5JVW"
    assert result.block_height == 187440904
    assert result.code_hash == "11111111111111111111111111111111"
    assert result.locked == "0"
    assert result.storage_paid_at == 0
    assert result.storage_usage == 410


def test_call_function_result_parsing():
    sample = {
        "jsonrpc": "2.0",
        "result": {
            "block_hash": "GTZdXfNmnL6TkJFdBeVMHCadgLuKChVfRNCSVsEQoJ7L",
            "block_height": 187444191,
            "logs": [],
            "result": [
                34,
                71,
                114,
                101,
                101,
                116,
                105,
                110,
                103,
                115,
                32,
                102,
                114,
                111,
                109,
                32,
                78,
                69,
                65,
                82,
                32,
                80,
                114,
                111,
                116,
                111,
                99,
                111,
                108,
                33,
                34,
            ],
        },
        "id": "dontcare",
    }

    result = CallFunctionResult.from_json_response(sample)

    assert result.block_hash == "GTZdXfNmnL6TkJFdBeVMHCadgLuKChVfRNCSVsEQoJ7L"
    assert result.block_height == 187444191
    assert result.logs == []
    assert isinstance(result.result, list)
    assert result.decoded_result() == '"Greetings from NEAR Protocol!"'
