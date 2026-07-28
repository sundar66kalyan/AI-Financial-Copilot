class AIInsights:

    @staticmethod
    def generate(spending, cashflow, health, accounts, transactions, budgets):

        insights = []

        # -----------------------
        # Spending
        # -----------------------
        income = spending.get("income", 0)
        expense = spending.get("expense", 0)

        if expense == 0:
            insights.append(
                "💰 No expenses have been recorded yet. Start tracking daily expenses for better financial insights."
            )

        if income > expense:
            insights.append(
                "✅ Your income is greater than your expenses, indicating a positive cash flow."
            )

        if income > 0:
            savings_rate = ((income - expense) / income) * 100

            if savings_rate >= 50:
                insights.append(
                    f"🎯 Excellent savings rate ({savings_rate:.1f}%). Consider investing surplus funds."
                )

        # -----------------------
        # Accounts
        # -----------------------
        if len(accounts) == 1:
            insights.append(
                "🏦 You currently have one financial account. Diversifying accounts may improve financial management."
            )

        # -----------------------
        # Transactions
        # -----------------------
        if len(transactions) < 5:
            insights.append(
                "📝 Very few transactions are available. More transaction history will improve AI recommendations."
            )

        # -----------------------
        # Budgets
        # -----------------------
        if len(budgets) == 0:
            insights.append(
                "📊 No budgets have been created. Setting budgets helps control spending."
            )

        elif len(budgets) == 1:
            insights.append(
                "📊 Consider creating multiple budgets for different spending categories."
            )

        # -----------------------
        # Financial Health
        # -----------------------
        score = health.get("score", 0)

        if score < 50:
            insights.append(
                "⚠️ Your financial health score is low. Continue adding financial data for more accurate analysis."
            )

        elif score < 80:
            insights.append(
                "👍 Your financial health is good, with room for improvement."
            )

        else:
            insights.append(
                "🏆 Excellent financial health. Maintain your current financial habits."
            )

        return insights
