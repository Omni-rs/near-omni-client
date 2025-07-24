import hashlib

import base58

from near_omni_client.crypto import KeyPairSecp256k1, PublicKey


def sha256(msg: str) -> bytes:
    return hashlib.sha256(msg.encode("utf-8")).digest()


def test_sign_and_verify_static_key_secp256k1():
    key_str = "Cqmi5vHc59U1MHhq7JCxTSJentvVBYMcKGUA7s7kwnKn"
    expected_pubkey = "secp256k1:45KcWwYt6MYRnnWFSxyQVkuu9suAzxoSkUMEnFNBi9kDayTo5YPUaqMWUrf7YHUDNMMj3w75vKuvfAMgfiFXBy28"
    expected_signature = (
        "3xamkuNXQr4HHLXygRdp42Q19BRs6X5vENHbVtj7duaphZpdaRR2dZD7NvxWHw2twFiUxCvYXue6ZDsWg77DWBxNb"
    )

    key_pair = KeyPairSecp256k1(key_str)
    message = sha256("message")
    signature = key_pair.sign(message)

    assert key_pair.public_key.to_string() == expected_pubkey
    assert base58.b58encode(signature.signature).decode() == expected_signature


def test_sign_and_verify_random_key_secp256k1():
    key_pair = KeyPairSecp256k1.from_random()
    message = sha256("message")
    signature = key_pair.sign(message)

    assert key_pair.verify(message, signature.signature)


def test_sign_and_verify_with_public_key_secp256k1():
    key_str = "Cqmi5vHc59U1MHhq7JCxTSJentvVBYMcKGUA7s7kwnKn"
    pubkey_str = "secp256k1:45KcWwYt6MYRnnWFSxyQVkuu9suAzxoSkUMEnFNBi9kDayTo5YPUaqMWUrf7YHUDNMMj3w75vKuvfAMgfiFXBy28"

    key_pair = KeyPairSecp256k1(key_str)
    message = sha256("message")
    signature = key_pair.sign(message)

    public_key = PublicKey.from_string(pubkey_str)
    assert public_key.verify(message, signature.signature)


def test_public_key_to_string_secp256k1():
    key_str = "Cqmi5vHc59U1MHhq7JCxTSJentvVBYMcKGUA7s7kwnKn"
    expected = "secp256k1:45KcWwYt6MYRnnWFSxyQVkuu9suAzxoSkUMEnFNBi9kDayTo5YPUaqMWUrf7YHUDNMMj3w75vKuvfAMgfiFXBy28"

    key_pair = KeyPairSecp256k1(key_str)
    assert key_pair.public_key.to_string() == expected


def test_convert_to_string_roundtrip_secp256k1():
    key_pair = KeyPairSecp256k1.from_random()
    key_string = key_pair.to_string()

    assert key_string.startswith("secp256k1:")
    restored = KeyPairSecp256k1(key_string.split(":")[1])
    assert restored.secret_key == key_pair.secret_key

    static_str = "secp256k1:7s1Jno8tbqFHBMqLh3epaFBbk194zAuMqo8yPbxvTbXn"
    key_pair_2 = KeyPairSecp256k1(static_str.split(":")[1])
    assert key_pair_2.to_string() == static_str
