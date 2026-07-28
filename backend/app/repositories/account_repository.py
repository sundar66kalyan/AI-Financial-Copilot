from sqlalchemy.orm import Session

from backend.app.models.account import Account
from backend.app.schemas.account import AccountCreate


class AccountRepository:

    @staticmethod
    def create(
        db: Session,
        account: AccountCreate,
        user_id: int,
    ):

        db_account = Account(
            name=account.name,
            account_type=account.account_type,
            balance=account.balance,
            currency=account.currency,
            user_id=user_id,
        )

        db.add(db_account)
        db.commit()
        db.refresh(db_account)

        return db_account

    @staticmethod
    def get_all(
        db: Session,
        user_id: int,
    ):

        return (
            db.query(Account)
            .filter(Account.user_id == user_id)
            .all()
        )