from near_omni_client.chain_signatures.utils import get_evm_address, get_btc_legacy_address, get_btc_segwit_address

def test_get_evm_address():
    public_key_hex = (
        "04e612e7650febebc50b448bf790f6bdd70a8a6ce3b111a1d7e72c87afe84be7"
        "76e36226e3f89de1ba3cbb62c0f3fc05bffae672c9c59d5fa8a4737b6547c64eb7"
    )
    public_key = bytes.fromhex(public_key_hex)
    evm_addr = get_evm_address(public_key)

    expected_evm_addr = "0xd8d25820c9b9e2aa9cce55504355e500efcce715"
    assert evm_addr == expected_evm_addr, f"Expected {expected_evm_addr}, got {evm_addr}"


def test_get_btc_legacy_address():
    public_key_hex = (
        "04e612e7650febebc50b448bf790f6bdd70a8a6ce3b111a1d7e72c87afe84be7"
        "76e36226e3f89de1ba3cbb62c0f3fc05bffae672c9c59d5fa8a4737b6547c64eb7"
    )
    public_key = bytes.fromhex(public_key_hex)
    # For testnet, the expected legacy address (Base58Check) might be known.
    # Here, as an example, we check that the address starts with "m" or "n" (typical for testnet).
    legacy_addr = get_btc_legacy_address(public_key, network='testnet')
    assert legacy_addr[0] in ('m', 'n'), f"Unexpected testnet legacy address: {legacy_addr}"


def test_get_btc_segwit_address():
    public_key_hex = (
        "04e612e7650febebc50b448bf790f6bdd70a8a6ce3b111a1d7e72c87afe84be7"
        "76e36226e3f89de1ba3cbb62c0f3fc05bffae672c9c59d5fa8a4737b6547c64eb7"
    )
    public_key = bytes.fromhex(public_key_hex)
    segwit_addr = get_btc_segwit_address(public_key, network='testnet')
    # For testnet, segwit addresses typically start with "tb1"
    assert segwit_addr.startswith("tb1"), f"Unexpected testnet segwit address: {segwit_addr}"