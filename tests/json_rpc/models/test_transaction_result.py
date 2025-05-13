from near_omni_client.json_rpc.models import TransactionResult, TransactionSummary
from tests.json_rpc.mocks import mock_send_tx_response


def test_send_transaction_result_model_parsing():
    result = TransactionResult.from_json_response(mock_send_tx_response)

    assert result.final_execution_status == "FINAL"
    # transaction
    tx = result.transaction
    assert isinstance(tx, TransactionSummary)
    assert tx.nonce == 13
    assert tx.hash == "ASS7oYwGiem9HaNwJe6vS2kznx2CxueKDvU9BAYJRjNR"

    # transaction outcome
    o = result.transaction_outcome
    assert o.block_hash.startswith("9MzuZrR")
    assert o.outcome.gas_burnt == 223182562500

    # receipts outcome
    ro = result.receipts_outcome
    assert len(ro) == 2
    assert ro[1].outcome.tokens_burnt == "0"
