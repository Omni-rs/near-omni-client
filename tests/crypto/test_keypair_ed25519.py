import base58
import hashlib

from near_omni_client.crypto import KeyPairEd25519, PublicKey


def sha256(msg: str) -> bytes:
    return hashlib.sha256(msg.encode("utf-8")).digest()


def test_sign_and_verify_static_key():
    key_str = (
        "26x56YPzPDro5t2smQfGcYAPy3j7R2jB2NUb7xKbAGK23B6x4WNQPh3twb6oDksFov5X8ts5CtntUNbpQpAKFdbR"
    )
    expected_pubkey = "ed25519:AYWv9RAN1hpSQA4p1DLhCNnpnNXwxhfH9qeHN8B4nJ59"
    expected_signature = (
        "26gFr4xth7W9K7HPWAxq3BLsua8oTy378mC1MYFiEXHBBpeBjP8WmJEJo8XTBowetvqbRshcQEtBUdwQcAqDyP8T"
    )

    key_pair = KeyPairEd25519(key_str)
    message = hashlib.sha256("message".encode("utf-8")).digest()
    signature = key_pair.sign(message)

    assert key_pair.public_key.to_string() == expected_pubkey
    assert base58.b58encode(signature.signature).decode() == expected_signature


def test_sign_and_verify_random_key():
    key_pair = KeyPairEd25519.from_random()
    message = sha256("message")
    signature = key_pair.sign(message)
    assert key_pair.verify(message, signature.signature)


def test_sign_and_verify_with_public_key():
    base58_key_str = (
        "5JueXZhEEVqGVT5powZ5twyPP8wrap2K7RdAYGGdjBwiBdd7Hh6aQxMP1u3Ma9Yanq1nEv32EW7u8kUJsZ6f315C"
    )
    pubkey_str = "ed25519:EWrekY1deMND7N3Q7Dixxj12wD7AVjFRt2H9q21QHUSW"

    key_pair = KeyPairEd25519(base58_key_str)
    message = sha256("message")
    signature = key_pair.sign(message)

    public_key = PublicKey.from_string(pubkey_str)
    assert public_key.verify(message, signature.signature)


def test_public_key_to_string():
    key_str = (
        "5JueXZhEEVqGVT5powZ5twyPP8wrap2K7RdAYGGdjBwiBdd7Hh6aQxMP1u3Ma9Yanq1nEv32EW7u8kUJsZ6f315C"
    )
    expected = "ed25519:EWrekY1deMND7N3Q7Dixxj12wD7AVjFRt2H9q21QHUSW"

    key_pair = KeyPairEd25519(key_str)

    assert key_pair.public_key.to_string() == expected


def test_convert_to_string_roundtrip():
    key_pair = KeyPairEd25519.from_random()
    key_string = key_pair.to_string()

    assert key_string.startswith("ed25519:")
    restored = KeyPairEd25519(key_string.split(":")[1])

    assert restored.secret_key == key_pair.secret_key

    static_str = "ed25519:2wyRcSwSuHtRVmkMCGjPwnzZmQLeXLzLLyED1NDMt4BjnKgQL6tF85yBx6Jr26D2dUNeC716RBoTxntVHsegogYw"
    key_pair_2 = KeyPairEd25519(static_str.split(":")[1])

    assert key_pair_2.to_string() == static_str
