from pydantic import BaseModel
from pydantic import ConfigDict


class CategoryCreate(BaseModel):
    name: str
    category_type: str
    color: str = "#2196F3"
    icon: str = "wallet"


class CategoryResponse(BaseModel):
    id: int
    name: str
    category_type: str
    color: str
    icon: str
    is_active: bool
    user_id: int

    model_config = ConfigDict(
        from_attributes=True
    )