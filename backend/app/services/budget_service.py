from sqlalchemy.orm import Session

from backend.app.repositories.budget_repository import BudgetRepository
from backend.app.schemas.budget import BudgetCreate


class BudgetService:

    @staticmethod
    def create_budget(
        db: Session,
        budget: BudgetCreate,
        user_id: int,
    ):
        return BudgetRepository.create(
            db,
            budget,
            user_id,
        )

    @staticmethod
    def get_budgets(
        db: Session,
        user_id: int,
    ):
        return BudgetRepository.get_all(
            db,
            user_id,
        )