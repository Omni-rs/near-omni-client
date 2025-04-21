from pydantic import BaseModel
from typing import Optional, List, Literal

class Message(BaseModel):
    message: Optional[str]
    eventNonce: str
    attestation: Optional[str]
    cctpVersion: int
    status: Literal["pending_confirmations", "complete"]

class GetMessagesResponse(BaseModel):
    messages: List[Message]

class GetMessagesBadRequestResponse(BaseModel):
    error: str

class GetMessagesNotFoundResponse(BaseModel):
    code: int
    error: str