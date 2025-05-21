from .keypair_base import KeyPairBase
from .signature import Signature
from .public_key import PublicKey
from .types import KeyType, KeyPairString, KeySize

from nacl.signing import SigningKey
from nacl.encoding import RawEncoder
from nacl.exceptions import BadSignatureError
from base58 import b58encode, b58decode


class KeyPairEd25519(KeyPairBase):
    """
    Implements Ed25519 key pair functionality:
    - Accepts a base58-encoded extended secret key (32-byte secret + 32-byte public).
    - Provides signing, verification, and serialization.
    """

    def __init__(self, extended_secret_key: str):
        """
        Construct a KeyPairEd25519 from a base58-encoded extended secret key.
        The input must contain 64 bytes when decoded: 
        - first 32 bytes: secret key
        - next 32 bytes: public key
        """
        decoded = b58decode(extended_secret_key)
        if len(decoded) != KeySize.SECRET_KEY + KeySize.PUBLIC_KEY:
            raise ValueError("Invalid extended secret key length")

        # Split into secret and public key parts
        secret = decoded[:KeySize.SECRET_KEY]
        public = decoded[KeySize.SECRET_KEY:]

        # Create the internal SigningKey and VerifyKey from the secret
        self._signing_key = SigningKey(secret, encoder=RawEncoder)
        self._verify_key = self._signing_key.verify_key

        # Store the public key in our custom PublicKey format
        self._public_key = PublicKey(KeyType.ED25519, public)

        # Save the original base58-encoded extended key for reuse
        self._extended_secret_key = extended_secret_key

    @staticmethod
    def from_random() -> "KeyPairEd25519":
        """
        Generate a new random Ed25519 key pair.
        Returns a KeyPairEd25519 instance with a base58-encoded extended secret key.
        """
        sk = SigningKey.generate()
        pk = sk.verify_key.encode()
        extended = sk.encode() + pk  # 32-byte secret + 32-byte public
        return KeyPairEd25519(b58encode(extended).decode())

    def sign(self, message: bytes) -> Signature:
        """
        Sign the given message using the secret key.
        Returns a Signature object that includes both the raw signature and the public key.
        """
        signature = self._signing_key.sign(message).signature
        return Signature(signature=signature, public_key=self._public_key)

    def verify(self, message: bytes, signature: bytes) -> bool:
        """
        Verify that a signature is valid for the given message.
        Uses the stored public key to perform verification.
        """
        try:
            self._verify_key.verify(message, signature)
            return True
        except BadSignatureError:
            return False

    def get_public_key(self) -> PublicKey:
        """
        Return the public key corresponding to the private key.
        """
        return self._public_key

    def to_string(self) -> KeyPairString:
        """
        Return a serialized representation of the key pair as:
        'ed25519:<base58-encoded-extended-secret-key>'
        """
        return KeyPairString(f"{KeyType.ED25519}:{self._extended_secret_key}")
