import json
from enum import Enum
from typing import Any

import base58
from py_near_primitives import (
    AccessKey,
    AccessKeyPermissionFieldless,
    AddKeyAction,
    CreateAccountAction,
    DelegateAction,
    DeleteAccountAction,
    DeleteKeyAction,
    DeployContractAction,
    FunctionCallPermission,
    SignedDelegateAction,
    StakeAction,
    TransferAction,
)
from py_near_primitives import (
    FunctionCallAction as NearFunctionCallAction,
)


class ActionType(str, Enum):
    CREATE_ACCOUNT = "CreateAccount"
    DEPLOY_CONTRACT = "DeployContract"
    FUNCTION_CALL = "FunctionCall"
    TRANSFER = "Transfer"
    STAKE = "Stake"
    ADD_KEY = "AddKey"
    DELETE_KEY = "DeleteKey"
    DELETE_ACCOUNT = "DeleteAccount"
    DELEGATE = "Delegate"
    SIGNED_DELEGATE = "SignedDelegate"


class ActionFactory:
    @staticmethod
    def create_account() -> CreateAccountAction:
        return CreateAccountAction()

    @staticmethod
    def deploy_contract(code: bytes) -> DeployContractAction:
        return DeployContractAction(code)

    @staticmethod
    def function_call(
        method_name: str, args: bytes | dict[str, Any], gas: int, deposit: int
    ) -> NearFunctionCallAction:
        if isinstance(args, dict):
            args = json.dumps(args).encode("utf-8")
        return NearFunctionCallAction(method_name, args, gas, deposit)

    @staticmethod
    def transfer(deposit: int) -> TransferAction:
        return TransferAction(deposit)

    @staticmethod
    def stake(amount: int, public_key: str | bytes) -> StakeAction:
        if isinstance(public_key, str):
            key = base58.b58decode(public_key.replace("ed25519:", ""))
        else:
            key = public_key
        return StakeAction(amount, key)

    @staticmethod
    def add_full_access_key(public_key: str | bytes) -> AddKeyAction:
        if isinstance(public_key, str):
            key = base58.b58decode(public_key.replace("ed25519:", ""))
        else:
            key = public_key
        return AddKeyAction(
            public_key=key,
            access_key=AccessKey(0, AccessKeyPermissionFieldless.FullAccess),
        )

    @staticmethod
    def add_function_call_key(
        public_key: str | bytes, allowance: int, receiver_id: str, methods: list[str]
    ) -> AddKeyAction:
        if isinstance(public_key, str):
            key = base58.b58decode(public_key.replace("ed25519:", ""))
        else:
            key = public_key
        permission = FunctionCallPermission(receiver_id, methods, allowance)
        return AddKeyAction(public_key=key, access_key=AccessKey(0, permission))

    @staticmethod
    def delete_key(public_key: str | bytes) -> DeleteKeyAction:
        if isinstance(public_key, str):
            key = base58.b58decode(public_key.replace("ed25519:", ""))
        else:
            key = public_key
        return DeleteKeyAction(key)

    @staticmethod
    def delete_account(beneficiary_id: str) -> DeleteAccountAction:
        return DeleteAccountAction(beneficiary_id)

    @staticmethod
    def delegate(action: DelegateAction, signature: bytes) -> SignedDelegateAction:
        return SignedDelegateAction(delegate_action=action, signature=signature)

    @staticmethod
    def signed_delegate(action: DelegateAction, signature: bytes) -> SignedDelegateAction:
        return SignedDelegateAction(delegate_action=action, signature=signature)
