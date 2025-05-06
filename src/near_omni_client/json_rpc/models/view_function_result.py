from typing import List, Any


class ViewFunctionResult:
    block_hash: str
    block_height: str
    logs: List[str]
    result: Any

    def __init__(self, block_height, logs, result, block_hash=""):
        self.block_hash = block_hash
        self.block_height = block_height
        self.logs = logs
        self.result = result
