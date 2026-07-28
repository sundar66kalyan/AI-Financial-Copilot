from pydantic import BaseModel
from pydantic import ConfigDict


class AccountCreate(BaseModel):
    name: str
    account_type: str
    balance: float
    currency: str = "INR"


class AccountResponse(BaseModel):
    id: int
    name: str
    account_type: str
    balance: float
    currency: str
    is_active: bool
    user_id: int

    model_config = ConfigDict(
        from_attributes=True
    )