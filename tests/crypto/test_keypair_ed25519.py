import hashlib
import base58

from near_omni_client.crypto import KeyPairEd25519, PublicKey, KeyPair


def sha256(msg: str) -> bytes:
    return hashlib.sha256(msg.encode("utf-8")).digest()


def test_sign_and_verify():
    key_pair = KeyPairEd25519(
        "26x56YPzPDro5t2smQfGcYAPy3j7R2jB2NUb7xKbAGK23B6x4WNQPh3twb6oDksFov5X8ts5CtntUNbpQpAKFdbR"
    )
    assert key_pair.public_key.to_string() == "ed25519:AYWv9RAN1hpSQA4p1DLhCNnpnNXwxhfH9qeHN8B4nJ59"
    message = sha256("message")
    signature = key_pair.sign(message)
    print("Seed:", key_pair.secretKey)
    print("Public:", key_pair.publicKey.data.hex())
    print("Signature:", signature.signature.hex())
    print("Message:", message.hex())
    print("Verifies:", key_pair.verify(message, signature.signature))
    assert (
        base58.b58encode(signature.signature).decode()
        == "26gFr4xth7W9K7HPWAxq3BLsua8oTy378mC1MYFiEXHBBpeBjP8WmJEJo8XTBowetvqbRshcQEtBUdwQcAqDyP8T"
    )


def test_sign_and_verify_with_random():
    key_pair = KeyPairEd25519.from_random()
    message = sha256("message")
    signature = key_pair.sign(message)
    assert key_pair.verify(message, signature.signature)


def test_sign_and_verify_with_public_key():
    key_pair = KeyPairEd25519(
        "5JueXZhEEVqGVT5powZ5twyPP8wrap2K7RdAYGGdjBwiBdd7Hh6aQxMP1u3Ma9Yanq1nEv32EW7u8kUJsZ6f315C"
    )
    message = sha256("message")
    signature = key_pair.sign(message)
    public_key = PublicKey.from_string("ed25519:EWrekY1deMND7N3Q7Dixxj12wD7AVjFRt2H9q21QHUSW")
    assert public_key.verify(message, signature.signature)


def test_from_secret():
    key_pair = KeyPairEd25519(
        "5JueXZhEEVqGVT5powZ5twyPP8wrap2K7RdAYGGdjBwiBdd7Hh6aQxMP1u3Ma9Yanq1nEv32EW7u8kUJsZ6f315C"
    )
    assert key_pair.public_key.to_string() == "ed25519:EWrekY1deMND7N3Q7Dixxj12wD7AVjFRt2H9q21QHUSW"


def test_convert_to_string():
    key_pair = KeyPairEd25519.from_random()
    new_key_pair = KeyPair.from_string(key_pair.to_string())
    assert new_key_pair.secret_key == key_pair.secret_key

    key_string = "ed25519:2wyRcSwSuHtRVmkMCGjPwnzZmQLeXLzLLyED1NDMt4BjnKgQL6tF85yBx6Jr26D2dUNeC716RBoTxntVHsegogYw"
    key_pair2 = KeyPair.from_string(key_string)
    assert key_pair2.to_string() == key_string
