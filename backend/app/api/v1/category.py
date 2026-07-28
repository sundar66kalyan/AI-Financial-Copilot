from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.dependencies.auth import get_current_user
from backend.app.schemas.category import CategoryCreate, CategoryResponse
from backend.app.services.category_service import CategoryService

router = APIRouter(
    prefix="/api/v1/categories",
    tags=["Categories"],
)


@router.post(
    "",
    response_model=CategoryResponse,
)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return CategoryService.create_category(
        db=db,
        category=category,
        user_id=current_user.id,
    )


@router.get(
    "",
    response_model=list[CategoryResponse],
)
def get_categories(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return CategoryService.get_categories(
        db=db,
        user_id=current_user.id,
    )