from typing import Union

from py_near_primitives.py_near_primitives import (
    DelegateAction,
    TransferAction,
    DeleteAccountAction,
    FunctionCallAction,
    DeployContractAction,
    CreateAccountAction,
    SignedDelegateAction,
    DeleteKeyAction,
    AddKeyAction,
    StakeAction,
)

Action = Union[
    DelegateAction,
    TransferAction,
    DeleteAccountAction,
    FunctionCallAction,
    DeployContractAction,
    CreateAccountAction,
    SignedDelegateAction,
    DeleteKeyAction,
    AddKeyAction,
    StakeAction,
]
