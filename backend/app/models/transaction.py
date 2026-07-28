from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import relationship

from backend.app.database.db import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    title = Column(
        String(150),
        nullable=False,
    )

    description = Column(
        Text,
        nullable=True,
    )

    amount = Column(
        Float,
        nullable=False,
    )

    transaction_type = Column(
        String(20),
        nullable=False,
    )  # Income / Expense

    transaction_date = Column(
        DateTime,
        default=datetime.utcnow,
    )

    account_id = Column(
        Integer,
        ForeignKey("accounts.id"),
        nullable=False,
    )

    category_id = Column(
        Integer,
        ForeignKey("categories.id"),
        nullable=False,
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    user = relationship(
        "User",
        back_populates="transactions",
    )

    account = relationship(
        "Account",
        back_populates="transactions",
    )

    category = relationship(
        "Category",
        back_populates="transactions",
    )