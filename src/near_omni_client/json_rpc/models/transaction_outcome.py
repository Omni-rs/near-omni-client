from typing import List, Any
from near_omni_client.json_rpc.models.outcome import Outcome


# TODO: fix the Any type
class TransactionOutcome:
    proof: List[Any]
    block_hash: str
    id: str
    outcome: Outcome

    def __init__(self, data):
        self.id = data["id"]
        self.block_hash = data["block_hash"]
        self.proof = data["proof"]
        self.outcome = Outcome(data)
