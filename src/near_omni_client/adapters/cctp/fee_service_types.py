from pydantic import BaseModel


class Fee(BaseModel):
    """Model representing a fee in the fee service."""

    finalityThreshold: int
    minimumFee: int


class GetFeeResponse(BaseModel):
    """Response model for getting fees from the fee service."""

    data: list[Fee]


class GetFeesBadRequestResponse(BaseModel):
    """Response model for bad request errors when getting fees."""

    code: int
    message: str


class GetFeesNotFoundResponse(BaseModel):
    """Response model for not found errors when getting fees."""

    code: int
    message: str
