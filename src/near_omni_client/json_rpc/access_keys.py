from near_omni_client.json_rpc.interfaces.provider import IJsonRpcProvider
from near_omni_client.json_rpc.exceptions import JsonRpcError, ERRORS, ERROR_MESSAGES

class AccessKey:    
    def __init__(self, provider: IJsonRpcProvider):
        self.provider = provider

    async def view_access_key(self, account_id: str, public_key: str, finality: str = "final"):
        try:
            return await self.provider.call("query", {
                "request_type": "view_access_key",
                "finality": finality,
                "account_id": account_id,
                "public_key": public_key,
            })
        except JsonRpcError as e:
            error = ERRORS.get(e.cause)
            if error:
                raise error(str(e)) from e
            raise
        