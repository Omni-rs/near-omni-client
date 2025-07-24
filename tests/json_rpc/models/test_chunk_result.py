from near_omni_client.json_rpc.models import ChunkResult
from tests.json_rpc.mocks import mock_chunk_response


def test_chunk_result_model_parsing():
    result = ChunkResult.from_json_response(mock_chunk_response)

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
