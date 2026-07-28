from sqlalchemy.orm import Session

from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate


class TransactionRepository:

    @staticmethod
    def create(
        db: Session,
        transaction: TransactionCreate,
        user_id: int,
    ):

        db_transaction = Transaction(
            title=transaction.title,
            description=transaction.description,
            amount=transaction.amount,
            transaction_type=transaction.transaction_type,
            account_id=transaction.account_id,
            category_id=transaction.category_id,
            user_id=user_id,
        )

        db.add(db_transaction)
        db.commit()
        db.refresh(db_transaction)

        return db_transaction

    @staticmethod
    def get_all(
        db: Session,
        user_id: int,
    ):

        return (
            db.query(Transaction)
            .filter(Transaction.user_id == user_id)
            .all()
        )
