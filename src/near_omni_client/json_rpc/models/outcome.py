from typing import List


class Outcome:
    logs: List[str]
    receipt_ids: List[str]
    gas_burnt: int
    tokens_burnt: str
    status: dict

    def __init__(self, data):
        self.logs = data["outcome"]["logs"]
        self.receipt_ids = data["outcome"]["receipt_ids"]
        self.status = data["outcome"]["status"]
        self.tokens_burnt = data["outcome"]["tokens_burnt"]
        self.gas_burnt = data["outcome"]["gas_burnt"]
