import base58

from py_near_primitives import (
    CreateAccountAction,
    DeployContractAction,
    FunctionCallAction as NearFunctionCallAction,
    TransferAction,
    StakeAction,
    AddKeyAction,
    DeleteKeyAction,
    DeleteAccountAction,
    DelegateAction,
    SignedDelegateAction,
    AccessKey,
    AccessKeyPermissionFieldless,
    FunctionCallPermission,
)
from near_omni_client.transactions import ActionFactory


def test_create_account():
    act = ActionFactory.create_account()
    assert isinstance(act, CreateAccountAction)


def test_deploy_contract():
    code = b"\x00\x01\x02"
    act = ActionFactory.deploy_contract(code)
    assert isinstance(act, DeployContractAction)
    assert act.code == code


def test_function_call():
    method = "foo"
    args = {"x": 1}
    gas = 1000
    deposit = 5
    act = ActionFactory.function_call(method, args, gas, deposit)
    assert isinstance(act, NearFunctionCallAction)
    assert act.method_name == method
    assert act.args == args
    assert act.gas == gas
    assert act.deposit == deposit


def test_transfer():
    deposit = 123456
    act = ActionFactory.transfer(deposit)
    assert isinstance(act, TransferAction)
    assert act.deposit == deposit


def test_stake_bytes_and_string():
    amount = 777
    pk = b"\x03" * 32
    # con bytes
    act1 = ActionFactory.stake(amount, pk)
    assert isinstance(act1, StakeAction)
    assert act1.stake == amount
    assert act1.public_key == pk
    # con string base58 + prefijo ed25519:
    pk_str = "ed25519:" + base58.b58encode(pk).decode()
    act2 = ActionFactory.stake(amount, pk_str)
    assert act2.public_key == pk


def test_add_full_access_key():
    pk = b"\x04" * 32
    act = ActionFactory.add_full_access_key(pk)
    assert isinstance(act, AddKeyAction)
    assert act.public_key == pk
    assert isinstance(act.access_key, AccessKey)
    assert act.access_key.nonce == 0
    assert act.access_key.permission == AccessKeyPermissionFieldless.FullAccess

    # también acepta string con o sin prefijo
    pk_str = base58.b58encode(pk).decode()
    act2 = ActionFactory.add_full_access_key("ed25519:" + pk_str)
    assert act2.public_key == pk


def test_add_function_call_key():
    pk = b"\x05" * 32
    pk_str = "ed25519:" + base58.b58encode(pk).decode()
    allowance = 111
    receiver = "contract.testnet"
    methods = ["m1", "m2"]
    act = ActionFactory.add_function_call_key(pk_str, allowance, receiver, methods)
    assert isinstance(act, AddKeyAction)
    assert act.public_key == pk
    perm = act.access_key.permission
    assert isinstance(perm, FunctionCallPermission)
    assert perm.allowance == allowance
    assert perm.receiver_id == receiver
    assert perm.method_names == methods


def test_delete_key_and_account():
    pk = b"\x06" * 32
    pk_str = "ed25519:" + base58.b58encode(pk).decode()
    act1 = ActionFactory.delete_key(pk)
    assert isinstance(act1, DeleteKeyAction)
    assert act1.public_key == pk
    act2 = ActionFactory.delete_key(pk_str)
    assert act2.public_key == pk

    beneficiary = "beneficiary.testnet"
    act3 = ActionFactory.delete_account(beneficiary)
    assert isinstance(act3, DeleteAccountAction)
    assert act3.beneficiary_id == beneficiary


def test_delegate_and_signed_delegate():
    dummy = DelegateAction("a", "b", [], 1, 2, b"\x07" * 32)
    signature = b"\x08" * 64
    act = ActionFactory.delegate(dummy, signature)
    assert isinstance(act, SignedDelegateAction)
    assert act.delegate_action == dummy
    assert act.signature == signature

    # alias signed_delegate
    act2 = ActionFactory.signed_delegate(dummy, signature)
    assert act2.delegate_action == dummy
    assert act2.signature == signature
