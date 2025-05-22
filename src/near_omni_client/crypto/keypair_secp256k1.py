import os
from base58 import b58encode, b58decode
from secp256k1 import PrivateKey as Secp256k1PrivateKey, PublicKey as Secp256k1PublicKey
from nacl.signing import SigningKey
from .types import KeySize, KeyPairString, KeyType
from .keypair_base import KeyPairBase
from .signature import Signature
from .public_key import PublicKey
from nacl.encoding import RawEncoder


# class KeyPairSecp256k1(KeyPairBase):
#     """
#     Implements secp256k1 key pair functionality:
#     - Accepts a base58-encoded extended secret key (32-byte secret + 64-byte public).
#     - Provides signing, verification, and serialization.
#     """

#     def __init__(self, extended_secret_key: str):
#         """
#         Construct a KeyPairSecp256k1 from a base58-encoded extended secret key.
#         The input must contain 96 bytes when decoded:
#         - first 32 bytes: secret key
#         - next 64 bytes: public key (without 0x04 prefix)
#         """
#         decoded = b58decode(extended_secret_key)
#         if len(decoded) != KeySize.SECRET_KEY + KeySize.PUBLIC_KEY_SECP256K1:
#             raise ValueError("Invalid extended secret key length")

#         secret = decoded[: KeySize.SECRET_KEY]
#         public = decoded[KeySize.SECRET_KEY :]

#         self._priv = Secp256k1PrivateKey(secret, raw=True)
#         self._pubkey = Secp256k1PublicKey(b"\x04" + public, raw=True)

#         self._public_key = PublicKey(KeyType.SECP256K1, public)
#         self._extended_secret_key = extended_secret_key

#     @staticmethod
#     def from_random() -> "KeyPairSecp256k1":
#         """
#         Generate a new random secp256k1 key pair.
#         Returns a KeyPairSecp256k1 instance with base58-encoded extended secret key.
#         """
#         sk = os.urandom(KeySize.SECRET_KEY)
#         priv = Secp256k1PrivateKey(sk, raw=True)
#         pub = priv.pubkey.serialize(compressed=False)[1:]  # drop 0x04 prefix
#         extended = sk + pub
#         return KeyPairSecp256k1(b58encode(extended).decode())

#     def sign(self, message: bytes) -> Signature:
#         """
#         Sign the given message using the secret key.
#         Returns a Signature object that includes both the raw signature and the public key.
#         """
#         rec_sig = self._priv.ecdsa_sign_recoverable(message, raw=True)
#         sig, recid = self._priv.ecdsa_recoverable_serialize(rec_sig)
#         return Signature(signature=sig + bytes([recid]), public_key=self._public_key)

#     def verify(self, message: bytes, signature: bytes) -> bool:
#         """
#         Verify that a signature is valid for the given message.
#         Uses the stored public key to perform verification.
#         """
#         try:
#             sig64 = signature[:64]
#             return self._pubkey.ecdsa_verify(sig64, message, raw=True)
#         except Exception:
#             return False

#     @property
#     def secret_key(self) -> str:
#         """
#         Return the base58-encoded secret key (32 bytes).
#         """
#         return b58encode(self._priv.private_key).decode()

#     @property
#     def public_key(self) -> PublicKey:
#         """
#         Return the public key corresponding to the private key.
#         """
#         return self._public_key


#     def to_string(self) -> KeyPairString:
#         """
#         Return a serialized representation of the key pair as:
#         'secp256k1:<base58-encoded-extended-secret-key>'
#         """
#         return KeyPairString(f"{KeyType.SECP256K1.value}:{self._extended_secret_key}")
class KeyPairSecp256k1(KeyPairBase):
    """
    Implements secp256k1 key pair functionality compatible with NEAR SDK:
    - Accepts a base58-encoded secret-only (32-byte) or extended secret key (32-byte secret + 64-byte public).
    - Always derives public key from secret for consistency with SDK.
    - Serializes to `<curve>:<input-key>` (param unchanged) mimicking JS behavior.
    """

    def __init__(self, key_string: str):
        decoded = b58decode(key_string)
        # Accept secret-only (32) or extended-full (96)
        if len(decoded) == KeySize.SECRET_KEY:
            secret = decoded
        elif len(decoded) == KeySize.SECRET_KEY + KeySize.PUBLIC_KEY_SECP256K1:
            secret = decoded[: KeySize.SECRET_KEY]
        else:
            raise ValueError("Invalid Secp256k1 key length")

        # Derive private and public
        priv = Secp256k1PrivateKey(secret, raw=True)
        pub_full = priv.pubkey.serialize(compressed=False)
        public = pub_full[1:]

        # Store fields
        self._priv = priv
        self._public_key = PublicKey(KeyType.SECP256K1, public)
        self._secret_key = b58encode(secret).decode()
        self._extended_secret_key = key_string  # keep input unchanged

    @staticmethod
    def from_random() -> "KeyPairSecp256k1":
        # generate 32-byte secret
        import os

        secret = os.urandom(KeySize.SECRET_KEY)
        priv = Secp256k1PrivateKey(secret, raw=True)
        pub_full = priv.pubkey.serialize(compressed=False)
        public = pub_full[1:]
        extended = secret + public
        return KeyPairSecp256k1(b58encode(extended).decode())

    def sign(self, message: bytes) -> Signature:
        rec_sig = self._priv.ecdsa_sign_recoverable(message, raw=True)
        sig, recid = self._priv.ecdsa_recoverable_serialize(rec_sig)
        return Signature(signature=sig + bytes([recid]), public_key=self._public_key)

    def verify(self, message: bytes, signature: bytes) -> bool:
        sig64 = signature[:64]
        return self._public_key.verify(message, sig64)

    @property
    def secret_key(self) -> str:
        return self._secret_key

    @property
    def public_key(self) -> PublicKey:
        return self._public_key

    def to_string(self) -> KeyPairString:
        # mimic JS: always return original input param
        return KeyPairString(f"{KeyType.SECP256K1.value}:{self._extended_secret_key}")
