from abc import ABC, abstractmethod

from .public_key import PublicKey
from .signature import Signature
from .types import KeyPairString


class KeyPairBase(ABC):
    @abstractmethod
    def sign(self, message: bytes) -> Signature:
        pass

    @abstractmethod
    def verify(self, message: bytes, signature: bytes) -> bool:
        pass

    @property
    @abstractmethod
    def public_key(self) -> PublicKey:
        pass

    @property
    @abstractmethod
    def secret_key(self) -> str:
        pass

    @abstractmethod
    def to_string(self) -> KeyPairString:
        pass
