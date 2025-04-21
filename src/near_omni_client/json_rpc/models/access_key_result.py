from typing import List, Optional
from pydantic import BaseModel, Field, RootModel


class FunctionCallPermission(BaseModel):
    allowance: Optional[str]
    method_names: List[str]
    receiver_id: str


class FullAccessPermission(RootModel[dict]):
    root: dict = Field(default_factory=dict)
    

class Permission(BaseModel):
    FunctionCall: Optional[FunctionCallPermission] = None
    FullAccess: Optional[FullAccessPermission] = None


class AccessKeyResult(BaseModel):
    block_hash: str
    block_height: int
    nonce: int
    permission: Permission

    @classmethod
    def from_json_response(cls, rpc_response: dict) -> "AccessKeyResult":
        return cls.model_validate(rpc_response["result"])
