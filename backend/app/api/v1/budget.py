from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.dependencies.auth import get_current_user

from backend.app.schemas.budget import (
    BudgetCreate,
    BudgetResponse,
)

from backend.app.services.budget_service import BudgetService

router = APIRouter(
    prefix="/api/v1/budgets",
    tags=["Budgets"],
)


@router.post(
    "",
    response_model=BudgetResponse,
)
def create_budget(
    budget: BudgetCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return BudgetService.create_budget(
        db=db,
        budget=budget,
        user_id=current_user.id,
    )


@router.get(
    "",
    response_model=list[BudgetResponse],
)
def get_budgets(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return BudgetService.get_budgets(
        db=db,
        user_id=current_user.id,
    )