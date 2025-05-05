from pydantic import BaseModel
from typing import List


class AccountResult(BaseModel):
    amount: str
    block_hash: str
    block_height: int
    code_hash: str
    locked: str
    storage_paid_at: int
    storage_usage: int

    @classmethod
    def from_json_response(cls, rpc_response: dict) -> "AccountResult":
        return cls.model_validate(rpc_response["result"])


class CallFunctionResult(BaseModel):
    block_hash: str
    block_height: int
    logs: List[str]
    result: List[int]  # bytes as list of integers

    @classmethod
    def from_json_response(cls, rpc_response: dict) -> "CallFunctionResult":
        return cls.model_validate(rpc_response["result"])

    def decoded_result(self) -> str:
        """Decodes the result from a list of integers to a UTF-8 string."""
        return bytes(self.result).decode("utf-8")
