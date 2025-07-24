from typing import Any

from pydantic import BaseModel


class ExecutionOutcomeStatus(BaseModel):
    SuccessValue: str | None = None
    SuccessReceiptId: str | None = None
    Failure: Any | None = None


class ExecutionOutcome(BaseModel):
    logs: list[str]
    receipt_ids: list[str]
    gas_burnt: int
    tokens_burnt: str
    executor_id: str
    status: ExecutionOutcomeStatus


class ExecutionOutcomeWithProof(BaseModel):
    proof: list[Any]
    block_hash: str
    id: str
    outcome: ExecutionOutcome


class TransactionSummary(BaseModel):
    signer_id: str
    public_key: str
    nonce: int
    receiver_id: str
    actions: list[dict[str, Any]]
    signature: str
    hash: str


class TransactionResult(BaseModel):
    final_execution_status: str
    status: dict[str, Any]
    transaction: TransactionSummary
    transaction_outcome: ExecutionOutcomeWithProof
    receipts_outcome: list[ExecutionOutcomeWithProof]

    @classmethod
    def from_json_response(cls, rpc_response: dict) -> "TransactionResult":
        return cls.model_validate(rpc_response["result"])
