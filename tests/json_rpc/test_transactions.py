import pytest
from near_omni_client.json_rpc.transactions import Transactions, TxExecutionStatus
from near_omni_client.json_rpc.models import TransactionResult
from tests.json_rpc.mocks import MockProvider, mock_send_tx_response


@pytest.mark.asyncio
async def test_send_transaction():
    provider = MockProvider(mock_send_tx_response)
    tx_client = Transactions(provider)
    signed = "ZmFrZV9zaWduZWRfYnFhc2U="  # dummy base64
    result = await tx_client.send_transaction(
        signed_tx_base64=signed, wait_until=TxExecutionStatus.FINAL
    )

    assert isinstance(result, TransactionResult)
    assert result.final_execution_status == "FINAL"
    assert result.transaction.nonce == 13
