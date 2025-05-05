from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field


class FunctionCallPermission(BaseModel):
    allowance: Optional[str]
    method_names: List[str]
    receiver_id: str


class FullAccessPermission(BaseModel):
    pass


class Permission(BaseModel):
    model_config = ConfigDict(validate_by_alias=True)

    function_call: Optional[FunctionCallPermission] = Field(
        default=None, validation_alias="FunctionCall"
    )
    full_access: Optional[FullAccessPermission] = Field(default=None, validation_alias="FullAccess")


class AccessKeyResult(BaseModel):
    block_hash: str
    block_height: int
    nonce: int
    permission: Permission

    @classmethod
    def from_json_response(cls, rpc_response: dict) -> "AccessKeyResult":
        return cls.model_validate(rpc_response["result"])
