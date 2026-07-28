from backend.app.llm.gemini_client import generate_response


class InvestmentAgent:

    @staticmethod
    def recommend(health: dict):

        prompt = f"""
You are a professional financial advisor.

Financial Health:
{health}

Provide:

1. Risk Profile
2. Investment Strategy
3. Mutual Fund Advice
4. ETF Advice
5. Emergency Fund Recommendation
6. Retirement Planning
7. Action Plan

Keep the answer concise and practical.
"""

        return generate_response(prompt)