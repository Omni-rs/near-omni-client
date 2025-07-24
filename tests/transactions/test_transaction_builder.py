import pytest
from py_near_primitives import Transaction as NearTransaction

from near_omni_client.transactions import ActionFactory, TransactionBuilder


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
    create_account_action = ActionFactory.create_account()

    tx = (
        TransactionBuilder()
        .with_signer_id(signer_id)
        .with_public_key(public_key)
        .with_nonce(nonce)
        .with_receiver(receiver_id)
        .with_block_hash(block_hash)
        .add_action(create_account_action)
        .build()
    )

    assert isinstance(tx, NearTransaction)
    assert tx.signer_id == signer_id
    assert bytes(tx.public_key) == public_key
    assert tx.nonce == nonce
    assert tx.receiver_id == receiver_id
    assert bytes(tx.block_hash) == block_hash
