from near_omni_client.chain_signatures import Kdf


def test_derive_epsilon():
    account_id = "omnitester.testnet"
    path = "bitcoin-1"
    epsilon = Kdf.derive_epsilon(account_id, path)

    assert isinstance(epsilon, int)
    assert epsilon > 0


def test_derive_public_key_bitcoin():
    account_id = "omnitester.testnet"
    path = "bitcoin-1"
    derived_pub_bytes = Kdf.get_derived_public_key(account_id, path, "testnet")
    derived_pub_hex = derived_pub_bytes.hex()

    expected_hex = (
        "0471f75dc56b971fbe52dd3e80d2f8532eb8905157556df39cb7338a67c804126"
        "40c869f717217ba5b916db6d7dc7d6a84220f8251e626adad62cac9c7d6f8e032"
    )
    assert derived_pub_hex == expected_hex


def test_derive_public_key_ethereum():
    account_id = "omnitester.testnet"
    path = "ethereum-1"
    derived_pub_bytes = Kdf.get_derived_public_key(account_id, path, "testnet")
    derived_pub_hex = derived_pub_bytes.hex()

    expected_hex = (
        "04e612e7650febebc50b448bf790f6bdd70a8a6ce3b111a1d7e72c87afe84be7"
        "76e36226e3f89de1ba3cbb62c0f3fc05bffae672c9c59d5fa8a4737b6547c64eb7"
    )
    assert derived_pub_hex == expected_hex
