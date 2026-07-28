from backend.app.analytics.spending import SpendingAnalytics
from backend.app.analytics.cashflow import CashFlowAnalyzer

from backend.app.llm.gemini_client import generate_response


class AIService:

    @staticmethod
    def ask_finance_copilot(db, user_id: int, question: str):

        spending = SpendingAnalytics.summary(db, user_id)

        cashflow = CashFlowAnalyzer.analyze(db, user_id)

        health = {
            "status": "Financial Health module coming soon"
        }

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