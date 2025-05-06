from typing import List

from near_omni_client.json_rpc.models.transaction_data import TransactionData
from near_omni_client.json_rpc.models.receipt_outcome import ReceiptOutcome
from near_omni_client.json_rpc.models.transaction_outcome import TransactionOutcome
from near_omni_client.json_rpc.models.receipt import Receipt


class TransactionResult:
    receipt_outcome: List[ReceiptOutcome]
    receipts: List[dict] = []
    transaction_outcome: ReceiptOutcome
    status: dict
    transaction: TransactionData

    def __init__(self, receipts_outcome, transaction_outcome, transaction, status, **kargs):
        self.status = status
        self.transaction = TransactionData(**transaction)
        self.transaction_outcome = ReceiptOutcome(transaction_outcome)
        if "receipts" in kargs:
            self.receipts = kargs["receipts"]

        self.receipt_outcome = []
        for ro in receipts_outcome:
            self.receipt_outcome.append(ReceiptOutcome(ro))

    @property
    def logs(self):
        logs = self.transaction_outcome.logs
        for ro in self.receipt_outcome:
            logs.extend(ro.logs)
        return logs
