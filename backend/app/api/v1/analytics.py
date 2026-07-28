from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.analytics.spending import SpendingAnalytics
from app.analytics.financial_health import FinancialHealthAnalyzer
from app.database.session import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/api/v1/analytics",
    tags=["Analytics"],
)


@router.get("/spending")
def spending_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return SpendingAnalytics.summary(
        db,
        current_user.id,
    )


@router.get("/financial-health")
def financial_health(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return FinancialHealthAnalyzer.analyze(db, current_user.id)
