from app.analytics.spending import SpendingAnalytics
from app.analytics.cashflow import CashFlowAnalyzer


class FinancialHealthAnalyzer:

    @staticmethod
    def analyze(db, user_id: int):

        spending = SpendingAnalytics.summary(db, user_id)
        cashflow = CashFlowAnalyzer.analyze(db, user_id)

        total_income = cashflow.get("total_income", 0)
        total_expense = cashflow.get("total_expense", 0)
        net_balance = cashflow.get("net_balance", 0)

        if total_income == 0:
            return {
                "score": 0,
                "status": "No financial data available"
            }

        savings_rate = (net_balance / total_income) * 100
        expense_ratio = (total_expense / total_income) * 100

        score = 100

        if savings_rate < 20:
            score -= 30
        elif savings_rate < 40:
            score -= 15

        if expense_ratio > 80:
            score -= 30
        elif expense_ratio > 60:
            score -= 15

        if score >= 90:
            status = "Excellent"
        elif score >= 75:
            status = "Good"
        elif score >= 60:
            status = "Fair"
        else:
            status = "Poor"

        return {
            "score": score,
            "status": status,
            "savings_rate": round(savings_rate, 2),
            "expense_ratio": round(expense_ratio, 2),
            "net_balance": net_balance,
        }
