from abc import ABC, abstractmethod
from typing import Any


# TODO: Fix the Any return type
class IJsonRpcProvider(ABC):
    @abstractmethod
    async def call(self, method: str, params: dict) -> Any:
        pass
