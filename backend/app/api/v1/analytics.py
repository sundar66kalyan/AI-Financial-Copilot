from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.app.analytics.cashflow import CashFlowAnalyzer

from backend.app.database.session import get_db

from backend.app.dependencies.auth import get_current_user

router = APIRouter(
    prefix="/api/v1/analytics",
    tags=["Analytics"],
)


@router.get("/cashflow")
def cashflow(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    return CashFlowAnalyzer.analyze(
        db,
        current_user.id,
    )