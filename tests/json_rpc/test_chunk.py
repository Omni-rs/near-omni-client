import pytest

from near_omni_client.json_rpc.chunk import Chunk
from near_omni_client.json_rpc.models import ChunkResult
from tests.json_rpc.mocks import MockProvider
from tests.json_rpc.mocks import mock_chunk_response


@pytest.mark.asyncio
async def test_view_chunk_by_chunk_id():
    provider = MockProvider(mock_chunk_response)
    blocks = Chunk(provider)

    result = await blocks.view_chunk(chunk_id="CzPafxtJmM1FnRoasKWAVhceJzZzkz9RKUBQQ4kY9V1v")

    assert isinstance(result, ChunkResult)

    assert result.author == "kiln.pool.f863973.m0"
    h = result.header
    assert h.chunk_hash == "CzPafxtJmM1FnRoasKWAVhceJzZzkz9RKUBQQ4kY9V1v"
    assert h.shard_id == 0
    assert h.gas_used == 0
    assert h.bandwidth_requests is None

    # receipts empty
    assert result.receipts == []

    # transactions
    txs = result.transactions
    assert len(txs) == 1
    tx = txs[0]
    assert tx.hash.startswith("J3KbUXF9")

    # actions inside transaction
    act = tx.actions[0].function_call
    assert act.method_name == "write_record"
    assert act.args.startswith("eyJyZWNvcmR")


@pytest.mark.asyncio
async def test_view_chunk_by_block_and_shard():
    provider = MockProvider(mock_chunk_response)
    blocks = Chunk(provider)

    result = await blocks.view_chunk(block_id=187310138, shard_id=0)

    assert isinstance(result, ChunkResult)
    assert result.header.height_included == 187310138
    assert result.header.shard_id == 0


@pytest.mark.asyncio
async def test_view_chunk_invalid_params():
    provider = MockProvider(mock_chunk_response)
    blocks = Chunk(provider)

    # no params
    with pytest.raises(ValueError):
        await blocks.view_chunk()

    # both chunk_id and block_id
    with pytest.raises(ValueError):
        await blocks.view_chunk(chunk_id="foo", block_id=123, shard_id=0)

    # block_id without shard_id
    with pytest.raises(ValueError):
        await blocks.view_chunk(block_id=123)
