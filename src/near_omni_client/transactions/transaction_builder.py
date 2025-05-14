from typing import Any
from py_near_primitives import Transaction as NearTransaction


class TransactionBuilder:
    def __init__(self):
        self._signer_id: str | None = None
        self._public_key: bytes | None = None
        self._nonce: int | None = None
        self._receiver_id: str | None = None
        self._block_hash: bytes | None = None
        self._priority_fee: int | None = None
        self._actions: list[Any] = []

    def with_signer_id(self, signer_id: str) -> "TransactionBuilder":
        self._signer_id = signer_id
        return self

    def with_public_key(self, public_key: bytes) -> "TransactionBuilder":
        self._public_key = public_key
        return self

    def with_nonce(self, nonce: int) -> "TransactionBuilder":
        self._nonce = nonce
        return self

    def with_receiver(self, receiver_id: str) -> "TransactionBuilder":
        self._receiver_id = receiver_id
        return self

    def with_block_hash(self, block_hash: bytes) -> "TransactionBuilder":
        self._block_hash = block_hash
        return self

    def with_priority_fee(self, fee: int) -> "TransactionBuilder":
        self._priority_fee = fee
        return self

    def add_action(self, action: Any) -> "TransactionBuilder":
        self._actions.append(action)
        return self

    def build(self) -> NearTransaction:
        missing = [
            name
            for name, val in [
                ("signer_id", self._signer_id),
                ("public_key", self._public_key),
                ("nonce", self._nonce),
                ("receiver_id", self._receiver_id),
                ("block_hash", self._block_hash),
            ]
            if val is None
        ]
        if missing:
            raise ValueError(f"Missing required fields: {', '.join(missing)}")

        return NearTransaction(
            self._signer_id,  # type: ignore
            self._public_key,  # type: ignore
            self._nonce,  # type: ignore
            self._receiver_id,  # type: ignore
            self._block_hash,  # type: ignore
            self._actions,
            priority_fee=self._priority_fee,
        )
