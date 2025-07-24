import json

import base58
from py_near_primitives import (
    AccessKey,
    AddKeyAction,
    CreateAccountAction,
    DelegateAction,
    DeleteAccountAction,
    DeleteKeyAction,
    DeployContractAction,
    SignedDelegateAction,
    StakeAction,
    TransferAction,
)
from py_near_primitives import (
    FunctionCallAction as NearFunctionCallAction,
)

from near_omni_client.transactions import ActionFactory


def test_create_account():
    act = ActionFactory.create_account()

    assert isinstance(act, CreateAccountAction)


def test_deploy_contract_bytes_and_list():
    code_bytes = b"\x00\x01\x02"
    act = ActionFactory.deploy_contract(code_bytes)

    assert isinstance(act, DeployContractAction)

    assert act.code == list(code_bytes)


def test_function_call_with_bytes_and_dict():
    method = "foo"
    args_bytes = b"\x10\x20"
    gas, deposit = 1_000, 5

    # case bytes -> must be passed as bytes
    act1 = ActionFactory.function_call(method, args_bytes, gas, deposit)
    assert isinstance(act1, NearFunctionCallAction)
    assert act1.method_name == method
    assert act1.args == list(args_bytes)

    # case dict -> must be passed as dict and serialized to bytes
    payload = {"x": 1}
    act2 = ActionFactory.function_call(method, payload, gas, deposit)
    expected = json.dumps(payload).encode()
    assert act2.args == list(expected)


def test_transfer():
    deposit = 123_456
    act = ActionFactory.transfer(deposit)
    assert isinstance(act, TransferAction)
    assert act.deposit == deposit


def test_stake_bytes_and_string():
    amount = 777
    pk = b"\x03" * 32

    act1 = ActionFactory.stake(amount, pk)
    assert isinstance(act1, StakeAction)
    assert act1.stake == amount
    assert act1.public_key == list(pk)

    pk_str = "ed25519:" + base58.b58encode(pk).decode()
    act2 = ActionFactory.stake(amount, pk_str)
    assert act2.public_key == list(pk)


def test_add_full_access_key_bytes_and_str():
    pk = b"\x04" * 32
    act1 = ActionFactory.add_full_access_key(pk)

    assert isinstance(act1, AddKeyAction)
    assert act1.public_key == list(pk)
    assert isinstance(act1.access_key, AccessKey)
    assert act1.access_key.nonce == 0

    pk_str = base58.b58encode(pk).decode()
    act2 = ActionFactory.add_full_access_key("ed25519:" + pk_str)
    assert act2.public_key == list(pk)


def test_add_function_call_key():
    pk = b"\x05" * 32
    pk_str = "ed25519:" + base58.b58encode(pk).decode()
    allowance = 111
    receiver = "contract.testnet"
    methods = ["m1", "m2"]

    act = ActionFactory.add_function_call_key(pk_str, allowance, receiver, methods)
    assert isinstance(act, AddKeyAction)
    assert act.public_key == list(pk)  # because py_near_primitives returns List[int]

    assert isinstance(act.access_key, AccessKey)
    assert act.access_key.nonce == 0
    # No assertion on .permission, since it's not exposed


def test_delete_key_and_account():
    pk = b"\x06" * 32
    pk_str = "ed25519:" + base58.b58encode(pk).decode()

    act1 = ActionFactory.delete_key(pk)
    assert isinstance(act1, DeleteKeyAction)
    assert bytes(act1.public_key) == pk

    act2 = ActionFactory.delete_key(pk_str)
    assert bytes(act2.public_key) == pk

    beneficiary = "beneficiary.testnet"
    act3 = ActionFactory.delete_account(beneficiary)
    assert isinstance(act3, DeleteAccountAction)
    assert act3.beneficiary_id == beneficiary


def test_delegate_and_signed_delegate():
    dummy = DelegateAction("a", "b", [], 1, 2, b"\x07" * 32)
    signature = b"\x08" * 64

    act = ActionFactory.delegate(dummy, signature)
    assert isinstance(act, SignedDelegateAction)

    assert act.delegate_action.sender_id == dummy.sender_id
    assert act.delegate_action.receiver_id == dummy.receiver_id
    assert act.delegate_action.nonce == dummy.nonce
    assert act.delegate_action.max_block_height == dummy.max_block_height
    assert act.delegate_action.public_key == list(dummy.public_key)

    assert act.signature == list(signature)

    # alias
    act2 = ActionFactory.signed_delegate(dummy, signature)
    assert act2.signature == list(signature)
