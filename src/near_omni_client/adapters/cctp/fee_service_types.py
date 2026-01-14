from pydantic import BaseModel, RootModel


class Fee(BaseModel):
    """Model representing a fee in the fee service."""

    finalityThreshold: int
    minimumFee: float


class GetFeeResponse(RootModel[list[Fee]]):
    """Response model for getting fees from the fee service."""

    pass


class GetFeesBadRequestResponse(BaseModel):
    """Response model for bad request errors when getting fees."""

    code: int
    message: str


class GetFeesNotFoundResponse(BaseModel):
    """Response model for not found errors when getting fees."""

    code: int
    message: str
