import pytest

from near_omni_client.json_rpc.block import Block
from near_omni_client.json_rpc.models import BlockResult
from tests.json_rpc.mocks import MockProvider, mock_block_response


@pytest.mark.asyncio
async def test_view_block_by_finality():
    provider = MockProvider(mock_block_response)
    blocks = Block(provider)

    result = await blocks.view_block(finality="final")

    assert isinstance(result, BlockResult)
    assert result.author == "node2"
    # header.hash comes from "hash" in the JSON header
    assert result.header.hash == "6RWmTYhXCzjMjoY3Mz1rfFcnBm8E6XeDDbFEPUA4sv1w"
    # first chunk gas_used is 0 in the sample
    assert result.chunks[0].gas_used == 0


@pytest.mark.asyncio
async def test_view_block_by_height():
    provider = MockProvider(mock_block_response)
    blocks = Block(provider)

    result = await blocks.view_block(block_id=187310138)

    assert isinstance(result, BlockResult)
    assert result.header.height == 187310138
    assert result.chunks[0].shard_id == 0


@pytest.mark.asyncio
async def test_view_block_by_hash():
    provider = MockProvider(mock_block_response)
    blocks = Block(provider)

    # use the actual block hash from the sample
    block_hash = mock_block_response["result"]["header"]["hash"]
    result = await blocks.view_block(block_id=block_hash)

    assert isinstance(result, BlockResult)
    assert result.header.hash == block_hash
    assert result.chunks[0].chunk_hash == "CzPafxtJmM1FnRoasKWAVhceJzZzkz9RKUBQQ4kY9V1v"
