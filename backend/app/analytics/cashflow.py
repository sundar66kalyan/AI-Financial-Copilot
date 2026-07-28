from sqlalchemy.orm import Session

from backend.app.models.transaction import Transaction


class CashFlowAnalyzer:

    @staticmethod
    def analyze(db: Session, user_id: int):

        transactions = (
            db.query(Transaction)
            .filter(Transaction.user_id == user_id)
            .all()
        )

        income = 0
        expense = 0

        for t in transactions:

            if t.transaction_type == "Income":
                income += t.amount

            elif t.transaction_type == "Expense":
                expense += t.amount

        net = income - expense

        if income > 0:
            savings_rate = round((net / income) * 100, 2)
        else:
            savings_rate = 0

        return {
            "income": income,
            "expense": expense,
            "net_cashflow": net,
            "savings_rate": savings_rate,
            "transactions": len(transactions),
        }