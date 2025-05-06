from typing import List


class TransactionData:
    hash: str
    public_key: str
    receiver_id: str
    signature: str
    signer_id: str
    nonce: int
    actions: List[ReceiptAction]

    def __init__(
        self,
        hash,
        public_key,
        receiver_id,
        signature,
        signer_id,
        nonce,
        actions,
        **kargs,
    ):
        self.actions = [ReceiptAction.build(a) for a in actions]
        self.nonce = nonce
        self.signer_id = signer_id
        self.public_key = public_key
        self.receiver_id = receiver_id
        self.signature = signature
        self.hash = hash

    @property
    def url(self):
        return f"https://nearblocks.io/ru/txns/{self.hash}"
