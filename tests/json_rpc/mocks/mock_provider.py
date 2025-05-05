from near_omni_client.json_rpc.interfaces.provider import IJsonRpcProvider
from near_omni_client.json_rpc.exceptions import JsonRpcError


class MockProvider(IJsonRpcProvider):
    def __init__(self, response: dict):
        self.response = response

    async def call(self, method: str, params: dict):
        assert method == "query"
        assert params["request_type"] == "view_access_key"

        if "error" in self.response:
            raise JsonRpcError.from_response(self.response["error"])

        return self.response
