from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.dependencies.auth import get_current_user

from app.analytics.spending import SpendingAnalytics
from app.analytics.cashflow import CashFlowAnalyzer
from app.analytics.financial_health import FinancialHealthAnalyzer
from app.analytics.ai_insights import AIInsights

from app.services.account_service import AccountService
from app.services.transaction_service import TransactionService
from app.services.budget_service import BudgetService


router = APIRouter(
    prefix="/api/v1/insights",
    tags=["AI Insights"]
)


@router.get("/")
def get_ai_insights(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    spending = SpendingAnalytics.summary(db, current_user.id)

    cashflow = CashFlowAnalyzer.analyze(db, current_user.id)

    health = FinancialHealthAnalyzer.analyze(db, current_user.id)

    accounts = AccountService.get_accounts(db, current_user.id)

    transactions = TransactionService.get_transactions(db, current_user.id)

    budgets = BudgetService.get_budgets(db, current_user.id)

    insights = AIInsights.generate(
        spending=spending,
        cashflow=cashflow,
        health=health,
        accounts=accounts,
        transactions=transactions,
        budgets=budgets,
    )

    return {
        "financial_health": health,
        "spending": spending,
        "cashflow": cashflow,
        "insights": insights,
    }
