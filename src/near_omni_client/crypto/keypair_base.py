from abc import ABC, abstractmethod


class KeyPairBase(ABC):
    @abstractmethod
    def sign(self, message: bytes) -> bytes:
        pass

    @abstractmethod
    def verify(self, message: bytes, signature: bytes) -> bool:
        pass

    @abstractmethod
    def get_public_key(self) -> bytes:
        pass

    @abstractmethod
    def to_string(self) -> str:
        pass
