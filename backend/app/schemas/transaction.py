from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class TransactionCreate(BaseModel):
    title: str
    description: str | None = None
    amount: float
    transaction_type: str
    account_id: int
    category_id: int


class TransactionResponse(BaseModel):
    id: int
    title: str
    description: str | None
    amount: float
    transaction_type: str
    transaction_date: datetime
    account_id: int
    category_id: int
    user_id: int

    model_config = ConfigDict(
        from_attributes=True
    )