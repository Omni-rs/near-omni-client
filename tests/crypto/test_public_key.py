from near_omni_client.crypto import PublicKey, KeyType

import base58
import pytest


def test_public_key_from_too_short_string():
    too_short_key = b"tooShortPublicKey"
    encoded = base58.b58encode(too_short_key).decode()

    with pytest.raises(ValueError) as excinfo:
        PublicKey.from_string(encoded)

    assert f"Invalid public key size ({len(too_short_key)})" in str(excinfo.value)


def test_public_key_from_valid_string():
    # 32 bytes = valid Ed25519 public key
    valid_key = bytes.fromhex("0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF")
    encoded = base58.b58encode(valid_key).decode()

    pk = PublicKey.from_string(encoded)

    assert pk.key_type == KeyType.ED25519
    assert pk.data == valid_key
