class InvestmentAdvisor:

    @staticmethod
    def recommend(health: dict):

        score = health.get("score", 0)

        if score >= 90:
            return {
                "risk": "High",
                "recommendation": [
                    "Index Funds",
                    "ETFs",
                    "Stocks",
                    "Retirement Fund"
                ]
            }

        elif score >= 70:
            return {
                "risk": "Medium",
                "recommendation": [
                    "Balanced Mutual Funds",
                    "Index Funds",
                    "Gold ETF"
                ]
            }

        else:
            return {
                "risk": "Low",
                "recommendation": [
                    "High Yield Savings",
                    "Emergency Fund",
                    "Fixed Deposit"
                ]
            }
