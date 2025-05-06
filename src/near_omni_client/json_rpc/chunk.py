from typing import Union
from near_omni_client.json_rpc.interfaces.provider import IJsonRpcProvider
from near_omni_client.json_rpc.exceptions import JsonRpcError, ERRORS, ERROR_MESSAGES
from near_omni_client.json_rpc.models import ChunkResult


class Chunk:
    def __init__(self, provider: IJsonRpcProvider):
        self.provider = provider

    async def view_chunk(
        self,
        *,
        chunk_id: str | None = None,
        block_id: int | str | None = None,
        shard_id: int | None = None,
    ) -> ChunkResult:
        if chunk_id and (block_id is not None or shard_id is not None):
            raise ValueError("Cannot provide both chunk_id and (block_id + shard_id)")
        if not chunk_id and not (block_id is not None and shard_id is not None):
            raise ValueError("Must provide chunk_id or both block_id and shard_id")

        params: dict[str, Union[str, int]] = {}
        if chunk_id:
            params["chunk_id"] = chunk_id
        else:
            params["block_id"] = block_id  # type int o str
            params["shard_id"] = shard_id  # type int

        try:
            res = await self.provider.call("chunk", params)
            return ChunkResult.from_json_response(res)
        except JsonRpcError as e:
            error = ERRORS.get(e.cause_name)
            message = ERROR_MESSAGES.get(e.cause_name, str(e))
            if error:
                raise error(message) from e
            raise
