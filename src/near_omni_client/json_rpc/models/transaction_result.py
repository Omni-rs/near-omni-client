from typing import Any, List, Optional, Dict
from pydantic import BaseModel


class ExecutionOutcomeStatus(BaseModel):
    SuccessValue: Optional[str] = None
    SuccessReceiptId: Optional[str] = None
    Failure: Optional[Any] = None


class ExecutionOutcome(BaseModel):
    logs: List[str]
    receipt_ids: List[str]
    gas_burnt: int
    tokens_burnt: str
    executor_id: str
    status: ExecutionOutcomeStatus


class ExecutionOutcomeWithProof(BaseModel):
    proof: List[Any]
    block_hash: str
    id: str
    outcome: ExecutionOutcome


class TransactionSummary(BaseModel):
    signer_id: str
    public_key: str
    nonce: int
    receiver_id: str
    actions: List[Dict[str, Any]]
    signature: str
    hash: str


class TransactionResult(BaseModel):
    final_execution_status: str
    status: Dict[str, Any]
    transaction: TransactionSummary
    transaction_outcome: ExecutionOutcomeWithProof
    receipts_outcome: List[ExecutionOutcomeWithProof]

    @classmethod
    def from_json_response(cls, rpc_response: dict) -> "TransactionResult":
        return cls.model_validate(rpc_response["result"])
