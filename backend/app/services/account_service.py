from sqlalchemy.orm import Session

from app.repositories.account_repository import AccountRepository
from app.schemas.account import AccountCreate


class AccountService:

    @staticmethod
    def create_account(
        db: Session,
        account: AccountCreate,
        user_id: int,
    ):
        return AccountRepository.create(
            db,
            account,
            user_id,
        )

    @staticmethod
    def get_accounts(
        db: Session,
        user_id: int,
    ):
        return AccountRepository.get_all(
            db,
            user_id,
        )
