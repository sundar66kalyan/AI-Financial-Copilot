from pydantic import BaseModel
from pydantic import ConfigDict


class BudgetCreate(BaseModel):
    name: str
    category_id: int
    amount: float
    month: str
    year: int


class BudgetResponse(BaseModel):
    id: int
    category_id: int
    amount: float
    month: str
    year: int
    user_id: int

    model_config = ConfigDict(
        from_attributes=True
    )
