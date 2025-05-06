from typing import Any, List, Optional
from pydantic import BaseModel, Field
from .block_result import CongestionInfo


class ChunkHeader(BaseModel):
    balance_burnt: str
    bandwidth_requests: Optional[Any]
    chunk_hash: str
    congestion_info: CongestionInfo
    encoded_length: int
    encoded_merkle_root: str
    gas_limit: int
    gas_used: int
    height_created: int
    height_included: int
    outcome_root: str
    outgoing_receipts_root: str
    prev_block_hash: str
    prev_state_root: str
    rent_paid: str
    shard_id: int
    signature: str
    tx_root: str
    validator_proposals: List[Any]
    validator_reward: str


class FunctionCallAction(BaseModel):
    args: str
    deposit: str
    gas: int
    method_name: str


class Action(BaseModel):
    function_call: FunctionCallAction = Field(..., alias="FunctionCall")


class Transaction(BaseModel):
    actions: List[Action]
    hash: str
    nonce: int
    priority_fee: int
    public_key: str
    receiver_id: str
    signature: str
    signer_id: str


class ChunkResult(BaseModel):
    author: str
    header: ChunkHeader
    receipts: List[Any]
    transactions: List[Transaction]

    @classmethod
    def from_json_response(cls, rpc_response: dict) -> "ChunkResult":
        return cls.model_validate(rpc_response["result"])
