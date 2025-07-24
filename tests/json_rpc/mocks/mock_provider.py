from near_omni_client.json_rpc.exceptions import JsonRpcError
from near_omni_client.json_rpc.interfaces.provider import IJsonRpcProvider


class MockProvider(IJsonRpcProvider):
    supported_request_types = {
        "view_access_key_list",
        "view_access_key",
        "view_account",
        "call_function",
    }

    supported_methods = {"query", "block", "chunk", "send_tx"}

    def __init__(self, response: dict):
        self.response = response

    async def call(self, method: str, params: dict):
        assert method in self.supported_methods

        if method == "query":
            assert params["request_type"] in self.supported_request_types

        if "error" in self.response:
            raise JsonRpcError.from_response(self.response["error"])

        return self.response
