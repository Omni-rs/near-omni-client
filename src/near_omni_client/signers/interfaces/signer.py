from abc import ABC, abstractmethod


class ISigner(ABC):
    @abstractmethod
    def sign(self, data: bytes) -> bytes:
        pass
