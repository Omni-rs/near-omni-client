from pydantic import BaseModel, model_validator
from .access_key_result import Permission


class AccessKeyInner(BaseModel):
    nonce: int
    permission: Permission

    @model_validator(mode="before")
    @classmethod
    def parse_permission(cls, data):
        if isinstance(data, dict) and isinstance(data.get("permission"), str):
            if data["permission"] == "FullAccess":
                data["permission"] = {"FullAccess": {}}
        return data


class AccessKeyEntry(BaseModel):
    public_key: str
    access_key: AccessKeyInner


class AccessKeyListResult(BaseModel):
    block_hash: str
    block_height: int
    keys: list[AccessKeyEntry]

    @classmethod
    def from_json_response(cls, rpc_response: dict) -> "AccessKeyListResult":
        return cls.model_validate(rpc_response["result"])
