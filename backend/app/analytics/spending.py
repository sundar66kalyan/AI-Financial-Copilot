from sqlalchemy.orm import Session
from sqlalchemy import func

from backend.app.models.transaction import Transaction
from backend.app.models.category import Category


class SpendingAnalytics:

    @staticmethod
    def summary(db: Session, user_id: int):

        income = (
            db.query(func.sum(Transaction.amount))
            .filter(
                Transaction.user_id == user_id,
                Transaction.transaction_type == "Income"
            )
            .scalar()
            or 0
        )

        expense = (
            db.query(func.sum(Transaction.amount))
            .filter(
                Transaction.user_id == user_id,
                Transaction.transaction_type == "Expense"
            )
            .scalar()
            or 0
        )

        categories = (
            db.query(
                Category.name,
                func.sum(Transaction.amount)
            )
            .join(
                Transaction,
                Transaction.category_id == Category.id
            )
            .filter(
                Transaction.user_id == user_id,
                Transaction.transaction_type == "Expense"
            )
            .group_by(Category.name)
            .all()
        )

        expense_by_category = {
            name: float(amount)
            for name, amount in categories
        }

        return {
            "total_income": float(income),
            "total_expense": float(expense),
            "net_balance": float(income - expense),
            "expense_by_category": expense_by_category
        }