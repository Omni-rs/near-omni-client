from abc import ABC, abstractmethod


class ISigner(ABC):
    @abstractmethod
    def sign_bytes(self, data: bytes) -> bytes:
        pass
