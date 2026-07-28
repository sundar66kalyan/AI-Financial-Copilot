from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.dependencies.auth import get_current_user
from backend.app.schemas.transaction import (
    TransactionCreate,
    TransactionResponse,
)
from backend.app.services.transaction_service import TransactionService

router = APIRouter(
    prefix="/api/v1/transactions",
    tags=["Transactions"],
)


@router.post(
    "",
    response_model=TransactionResponse,
)
def create_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return TransactionService.create_transaction(
        db=db,
        transaction=transaction,
        user_id=current_user.id,
    )


@router.get(
    "",
    response_model=list[TransactionResponse],
)
def get_transactions(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return TransactionService.get_transactions(
        db=db,
        user_id=current_user.id,
    )