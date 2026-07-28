from sqlalchemy.orm import Session

from app.models.budget import Budget
from app.schemas.budget import BudgetCreate


class BudgetRepository:

    @staticmethod
    def create(
        db: Session,
        budget: BudgetCreate,
        user_id: int,
    ):
        db_budget = Budget(
            name=budget.name,
            category_id=budget.category_id,
            amount=budget.amount,
            month=budget.month,
            year=budget.year,
            user_id=user_id,
        )

        db.add(db_budget)
        db.commit()
        db.refresh(db_budget)

        return db_budget

    @staticmethod
    def get_all(
        db: Session,
        user_id: int,
    ):
        return (
            db.query(Budget)
            .filter(Budget.user_id == user_id)
            .all()
        )
