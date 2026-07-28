from backend.app.llm.gemini_client import generate_response


class ReportAgent:

    @staticmethod
    def generate(health: dict):

        prompt = f"""
You are a Certified Financial Planner.

Financial Summary:

{health}

Generate a professional report containing:

1. Executive Summary

2. Financial Health Score

3. Income vs Expense Analysis

4. Savings Analysis

5. Investment Opportunities

6. Risk Analysis

7. Budget Improvement Suggestions

8. Retirement Planning

9. Emergency Fund Analysis

10. Final Recommendations

Use proper headings.
"""

        return generate_response(prompt)