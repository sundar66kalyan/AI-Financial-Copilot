from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.dependencies.auth import get_current_user

from app.analytics.financial_health import FinancialHealthAnalyzer
from app.agents.investment_agent import InvestmentAgent

router = APIRouter(
    prefix="/api/v1/investment",
    tags=["Investment"]
)


@router.get("/recommendation")
def get_investment_recommendation(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    health = FinancialHealthAnalyzer.analyze(db, current_user.id)

    recommendation = InvestmentAgent.recommend(health)

    return {
        "financial_health": health,
        "ai_recommendation": recommendation
    }
