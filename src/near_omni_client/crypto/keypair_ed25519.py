from .keypair_base import KeyPairBase
from .signature import Signature
from .public_key import PublicKey
from .types import KeyType, KeyPairString, KeySize

from nacl.signing import SigningKey
from nacl.encoding import RawEncoder
from nacl.exceptions import BadSignatureError
from base58 import b58encode, b58decode


class KeyPairEd25519(KeyPairBase):
    def __init__(self, extended_secret_key: str):
        decoded = b58decode(extended_secret_key)
        if len(decoded) != KeySize.SECRET_KEY + KeySize.PUBLIC_KEY:
            raise ValueError("Invalid extended secret key length")

        secret = decoded[:KeySize.SECRET_KEY]
        public = decoded[KeySize.SECRET_KEY:]

        self._signing_key = SigningKey(secret, encoder=RawEncoder)
        self._verify_key = self._signing_key.verify_key
        self._public_key = PublicKey(KeyType.ED25519, public)
        self._extended_secret_key = extended_secret_key

    @staticmethod
    def from_random() -> "KeyPairEd25519":
        sk = SigningKey.generate()
        pk = sk.verify_key.encode()
        extended = sk.encode() + pk
        return KeyPairEd25519(b58encode(extended).decode())

    def sign(self, message: bytes) -> Signature:
        signature = self._signing_key.sign(message).signature
        return Signature(signature=signature, public_key=self._public_key)

    def verify(self, message: bytes, signature: bytes) -> bool:
        try:
            self._verify_key.verify(message, signature)
            return True
        except BadSignatureError:
            return False

    def get_public_key(self) -> PublicKey:
        return self._public_key

    def to_string(self) -> KeyPairString:
        return KeyPairString(f"{KeyType.ED25519}:{self._extended_secret_key}")
