from typing import Literal

from pydantic import BaseModel


class Message(BaseModel):
    message: str | None
    eventNonce: str
    attestation: str | None
    cctpVersion: int
    status: Literal["pending_confirmations", "complete"]


class GetMessagesResponse(BaseModel):
    messages: list[Message]


class GetMessagesBadRequestResponse(BaseModel):
    error: str


class GetMessagesNotFoundResponse(BaseModel):
    code: int
    error: str
