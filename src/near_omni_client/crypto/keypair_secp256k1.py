import os
from base58 import b58encode, b58decode
from secp256k1 import PrivateKey as Secp256k1PrivateKey, PublicKey as Secp256k1PublicKey
from nacl.signing import SigningKey
from .types import KeySize, KeyPairString, KeyType
from .keypair_base import KeyPairBase
from .signature import Signature
from .public_key import PublicKey
from nacl.encoding import RawEncoder


class KeyPairSecp256k1(KeyPairBase):
    """
    Implements secp256k1 key pair functionality compatible with NEAR SDK:
    - Accepts a base58-encoded secret-only (32-byte) or extended secret key (32-byte secret + 64-byte public).
    - Always derives public key from secret for consistency with SDK.
    - Serializes to `<curve>:<input-key>` (param unchanged) mimicking JS behavior.
    """

    def __init__(self, extended_secret_key: str):
        decoded = b58decode(extended_secret_key)
        secret = decoded[: KeySize.SECRET_KEY]  # 32 bytes
        self._priv = Secp256k1PrivateKey(secret, raw=True)
        pub_full = self._priv.pubkey.serialize(compressed=False)  # 65 bytes with 0x04 header
        public = pub_full[1:]  # 64 bytes without header
        self._public_key = PublicKey(KeyType.SECP256K1, public)
        self._secret_key = b58encode(secret).decode()
        self._extended_secret_key = extended_secret_key

    @staticmethod
    def from_random() -> "KeyPairSecp256k1":
        secret = os.urandom(KeySize.SECRET_KEY)
        priv = Secp256k1PrivateKey(secret, raw=True)
        pub_full = priv.pubkey.serialize(compressed=False)
        public = pub_full[1:]
        extended = secret + public
        return KeyPairSecp256k1(b58encode(extended).decode())

    def sign(self, message: bytes) -> Signature:
        # Use ecdsa_sign_recoverable to get a recoverable signature
        rec_sig = self._priv.ecdsa_sign_recoverable(message, raw=True)
        # Serialize with recovery ID
        sig, recid = self._priv.ecdsa_recoverable_serialize(rec_sig)
        # Return signature + recid byte (65 bytes total)
        return Signature(signature=sig + bytes([recid]), public_key=self._public_key)

    def verify(self, message: bytes, signature: bytes) -> bool:
        # Extract signature and recid
        sig_bytes, recid = signature[:-1], signature[-1]
        # Parse the signature with recovery info
        rec_sig = self._priv.ecdsa_recoverable_deserialize(sig_bytes, recid)
        # Convert to regular signature
        sig = self._priv.ecdsa_recoverable_convert(rec_sig)
        # Verify
        return self._priv.pubkey.ecdsa_verify(message, sig, raw=True)

    @property
    def secret_key(self) -> str:
        return self._secret_key

    @property
    def public_key(self) -> PublicKey:
        return self._public_key

    def to_string(self) -> KeyPairString:
        return KeyPairString(f"{KeyType.SECP256K1.value}:{self._extended_secret_key}")
