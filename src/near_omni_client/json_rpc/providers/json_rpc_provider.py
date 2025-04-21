import httpx
from typing import Any
from near_omni_client.json_rpc.interfaces.provider import IJsonRpcProvider

class JsonRpcError(Exception):
    def __init__(self, name, cause, info=None):
        self.name = name
        self.cause = cause
        self.info = info
        super().__init__(f"{name} ({cause}): {info}")

    @classmethod
    def from_response(cls, err: dict):
        name = err.get("name")
        cause = err.get("cause", {}).get("name")
        info = err.get("cause", {}).get("info")
        return cls(name=name, cause=cause, info=info)

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
