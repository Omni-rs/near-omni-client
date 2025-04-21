import httpx
from typing import Any
from near_omni_client.json_rpc.interfaces.provider import IJsonRpcProvider
from near_omni_client.json_rpc.exceptions import JsonRpcError

class JsonRpcProvider(IJsonRpcProvider):
    def __init__(self, rpc_url: str):
        self.rpc_url = rpc_url

    async def call(self, method: str, params: dict) -> Any:
        payload = {
            "jsonrpc": "2.0",
            "id": "dontcare",
            "method": method,
            "params": params,
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(self.rpc_url, json=payload)
            data = response.json()

            if "error" in data:
                raise JsonRpcError.from_response(data["error"])
            return data["result"]
