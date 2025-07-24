from near_omni_client.crypto import KeyPair, KeyPairEd25519, KeyPairSecp256k1


def test_convert_to_string_roundtrip_ed25519():
    key_pair = KeyPair.from_random("ed25519")
    key_string = key_pair.to_string()

    assert key_string.startswith("ed25519:")

    restored = KeyPair.from_string(key_string)
    assert isinstance(restored, KeyPairEd25519)
    assert restored.secret_key == key_pair.secret_key

    static_str = "ed25519:2wyRcSwSuHtRVmkMCGjPwnzZmQLeXLzLLyED1NDMt4BjnKgQL6tF85yBx6Jr26D2dUNeC716RBoTxntVHsegogYw"
    key_pair_2 = KeyPair.from_string(static_str)
    assert key_pair_2.to_string() == static_str


def test_convert_to_string_roundtrip_secp256k1():
    key_pair = KeyPair.from_random("secp256k1")
    key_string = key_pair.to_string()

    assert key_string.startswith("secp256k1:")

    restored = KeyPair.from_string(key_string)
    assert isinstance(restored, KeyPairSecp256k1)
    assert restored.secret_key == key_pair.secret_key

    static_str = "secp256k1:21HqLYoiJ5AEpERwGPbAt4rTSrHdhmvWSGkYPNAXjC6anetQ77oW1jRuVhv7vhEqmgvieMtZGitgbtGaUwMNMyPdVNVbsaHrYjBUeqrCZ4vHPm4Zvm67kmfLQZwC5asULqP1"
    key_pair_2 = KeyPair.from_string(static_str)
    assert key_pair_2.to_string() == static_str
