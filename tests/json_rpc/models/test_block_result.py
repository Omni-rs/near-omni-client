from near_omni_client.json_rpc.models import BlockResult
from tests.json_rpc.mocks import mock_block_response


def test_block_result_model_parsing():
    result = BlockResult.from_json_response(mock_block_response)

    # author & header
    assert result.author == "node2"
    assert result.header.hash == "6RWmTYhXCzjMjoY3Mz1rfFcnBm8E6XeDDbFEPUA4sv1w"
    assert result.header.approvals[0] is None  # null → None
    assert result.header.chunks_included == 6

    # chunks[0]
    c0 = result.chunks[0]
    assert c0.chunk_hash.startswith("CzPafxtJ")
    assert c0.congestion_info.allowed_shard == 1
    assert c0.bandwidth_requests is None  # null → None
    assert c0.validator_proposals == []  # empty list
    assert c0.balance_burnt == "0"

    # chunks[1]
    c1 = result.chunks[1]
    assert c1.shard_id == 1
    assert c1.gas_limit == 1000000000000000
