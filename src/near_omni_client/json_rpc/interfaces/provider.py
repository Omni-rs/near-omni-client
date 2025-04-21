from abc import ABC, abstractmethod
from typing import Any

class IJsonRpcProvider(ABC):
    @abstractmethod
    async def call(self, method: str, params: dict) -> Any:
        pass
