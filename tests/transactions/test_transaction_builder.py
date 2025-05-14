import pytest
from py_near_primitives import Transaction as NearTransaction
from near_omni_client.transactions import TransactionBuilder


def test_transaction_builder_missing_fields():
    builder = TransactionBuilder()
    with pytest.raises(ValueError) as exc:
        builder.build()
    msg = str(exc.value)
    # list of required fields:
    for field in ("signer_id", "public_key", "nonce", "receiver_id", "block_hash"):
        assert field in msg


def test_transaction_builder_success():
    signer_id = "alice.testnet"
    public_key = b"\x01" * 32
    nonce = 42
    receiver_id = "bob.testnet"
    block_hash = b"\x02" * 32
    priority_fee = 99
    dummy_action = object()

    tx = (
        TransactionBuilder()
        .with_signer_id(signer_id)
        .with_public_key(public_key)
        .with_nonce(nonce)
        .with_receiver(receiver_id)
        .with_block_hash(block_hash)
        .with_priority_fee(priority_fee)
        .add_action(dummy_action)
        .build()
    )

    assert isinstance(tx, NearTransaction)
    assert tx.signer_id == signer_id
    assert tx.public_key == public_key
    assert tx.nonce == nonce
    assert tx.receiver_id == receiver_id
    assert tx.block_hash == block_hash
    assert tx.actions == [dummy_action]
    assert getattr(tx, "priority_fee", None) == priority_fee
