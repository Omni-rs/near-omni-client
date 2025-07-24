from typing import Any

from pydantic import BaseModel, ConfigDict, Field, model_validator


class FunctionCallPermission(BaseModel):
    allowance: str | None
    method_names: list[str]
    receiver_id: str


class FullAccessPermission(BaseModel):
    pass


class Permission(BaseModel):
    model_config = ConfigDict(validate_by_alias=True)

    function_call: FunctionCallPermission | None = Field(
        default=None, validation_alias="FunctionCall"
    )
    full_access: FullAccessPermission | None = Field(default=None, validation_alias="FullAccess")


class AccessKeyResult(BaseModel):
    block_hash: str
    block_height: int
    nonce: int
    permission: str | Permission

    @classmethod
    def from_json_response(cls, rpc_response: dict) -> "AccessKeyResult":
        return cls.model_validate(rpc_response["result"])

    @model_validator(mode="before")
    @classmethod
    def transform_permission(cls, data: dict[str, Any]) -> dict[str, Any]:
        # only if permission is a string "FullAccess", transform it
        if isinstance(data.get("permission"), str) and data["permission"] == "FullAccess":
            data["permission"] = {"FullAccess": {}}
        return data
