from sqlalchemy.orm import Session

from app.repositories.transaction_repository import TransactionRepository
from app.schemas.transaction import TransactionCreate


class TransactionService:

    @staticmethod
    def create_transaction(
        db: Session,
        transaction: TransactionCreate,
        user_id: int,
    ):
        return TransactionRepository.create(
            db,
            transaction,
            user_id,
        )

    @staticmethod
    def get_transactions(
        db: Session,
        user_id: int,
    ):
        return TransactionRepository.get_all(
            db,
            user_id,
        )
