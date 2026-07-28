from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.dependencies.auth import get_current_user
from app.schemas.account import AccountCreate, AccountResponse
from app.services.account_service import AccountService

router = APIRouter(
    prefix="/api/v1/accounts",
    tags=["Accounts"],
)


@router.post(
    "",
    response_model=AccountResponse,
)
def create_account(
    account: AccountCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return AccountService.create_account(
        db=db,
        account=account,
        user_id=current_user.id,
    )


@router.get(
    "",
    response_model=list[AccountResponse],
)
def get_accounts(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return AccountService.get_accounts(
        db=db,
        user_id=current_user.id,
    )
