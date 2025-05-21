import os
import base58
from secp256k1 import PrivateKey as Secp256k1PrivateKey, PublicKey as Secp256k1PublicKey

from .types import KeySize, KeyPairString
from .keypair_base import KeyPairBase


class KeyPairSecp256k1(KeyPairBase):
    """
    Python implementation of secp256k1 key pair functionality.
    Generates key pairs, signs messages with recoverable ECDSA, and verifies signatures.
    nearcore expects 64-byte public keys (without the 0x04 header byte).
    """

    def __init__(self, extended_secret_key: str):
        super().__init__()
        # Decode the extended secret key from Base58 to bytes
        decoded = base58.b58decode(extended_secret_key)
        # Extract the first 32 bytes as the secret key
        secret_key_bytes = decoded[: KeySize.SECRET_KEY]
        # Initialize a secp256k1 PrivateKey
        self._priv = Secp256k1PrivateKey(secret_key_bytes, raw=True)
        # Serialize the uncompressed public key (65 bytes, including 0x04 header)
        pub_full = self._priv.pubkey.serialize(compressed=False)
        # Store the secp256k1 PublicKey object for verification
        self.public_key = Secp256k1PublicKey(pub_full, raw=True)
        # Store the Base58-encoded secret key and the extended key
        self.secret_key = base58.b58encode(secret_key_bytes).decode()
        self.extended_secret_key = extended_secret_key

    @classmethod
    def from_random(cls) -> "KeyPairSecp256k1":
        """
        Generate a new random secp256k1 key pair.
        Returns an instance with Base58-encoded extended secret key.
        """
        # Generate 32 random bytes for the secret key
        secret_key_bytes = os.urandom(KeySize.SECRET_KEY)
        # Initialize PrivateKey to derive the public key
        priv = Secp256k1PrivateKey(secret_key_bytes, raw=True)
        # Serialize the uncompressed public key
        pub_full = priv.pubkey.serialize(compressed=False)
        # Concatenate secret and public bytes, then Base58-encode
        extended = secret_key_bytes + pub_full[1:]
        encoded_ext = base58.b58encode(extended).decode()
        return cls(encoded_ext)

    def sign(self, message: bytes) -> bytes:
        """
        Sign the given message hash and return a Signature object.
        The signature is 65 bytes: 64-byte signature + 1-byte recovery ID.
        """
        # Create a recoverable ECDSA signature
        rec_sig = self._priv.ecdsa_sign_recoverable(message, raw=True)
        # Serialize the recoverable signature to (64-byte sig, recovery ID)
        sig, recid = self._priv.ecdsa_recoverable_serialize(rec_sig)
        return sig + bytes([recid])

    def verify(self, message: bytes, signature: bytes) -> bool:
        """
        Verify a signature against the message using the stored secp256k1 PublicKey.
        Returns True if valid, False otherwise.
        """
        # split signature and recovery ID
        sig64 = signature[:64]
        # verify signature
        return self.public_key.ecdsa_verify(sig64, message, raw=True)

    def __str__(self) -> KeyPairString:
        # Return the key pair as a string in the format 'secp256k1:<extended_secret>'
        return f"secp256k1:{self.extended_secret_key}"
