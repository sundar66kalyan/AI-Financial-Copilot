from app.analytics.spending import SpendingAnalytics
from app.analytics.cashflow import CashFlowAnalyzer
from app.analytics.financial_health import FinancialHealthAnalyzer

from app.llm.gemini_client import generate_response

from app.services.account_service import AccountService
from app.services.transaction_service import TransactionService
from app.services.budget_service import BudgetService


class AIService:

    @staticmethod
    def ask_finance_copilot(db, user_id: int, question: str):

        spending = SpendingAnalytics.summary(db, user_id)

        cashflow = CashFlowAnalyzer.analyze(db, user_id)

        health = FinancialHealthAnalyzer.analyze(db, user_id)

        prompt = f"""
You are an AI Financial Advisor.

Financial Summary

Spending
{spending}

Cashflow
{cashflow}

Financial Health
{health}

User Question

{question}

Provide a concise financial recommendation.
"""

        return generate_response(prompt)

    @staticmethod
    def generate_financial_report(db, user_id: int):

        spending = SpendingAnalytics.summary(db, user_id)

        cashflow = CashFlowAnalyzer.analyze(db, user_id)

        health = FinancialHealthAnalyzer.analyze(db, user_id)

        accounts = AccountService.get_accounts(db, user_id)

        transactions = TransactionService.get_transactions(db, user_id)

        budgets = BudgetService.get_budgets(db, user_id)

        prompt = f"""
You are a Certified Financial Planner (CFP).

Below is the client's financial information.

Spending Summary
{spending}

Cash Flow
{cashflow}

Financial Health
{health}

Number of Accounts
{len(accounts)}

Number of Transactions
{len(transactions)}

Number of Budgets
{len(budgets)}

Generate a professional financial report.

Include:

1. Executive Summary
2. Financial Health Score
3. Income vs Expense Analysis
4. Savings Analysis
5. Budget Analysis
6. Investment Recommendations
7. Risk Analysis
8. Emergency Fund Analysis
9. Retirement Planning
10. Final Recommendations

Use ONLY the financial data provided.

Do NOT say:

'No financial data available'

unless the data is actually empty.
"""

        return generate_response(prompt)
