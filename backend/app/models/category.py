from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from backend.app.database.db import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    name = Column(
        String(100),
        nullable=False,
    )

    category_type = Column(
        String(30),
        nullable=False,
    )  # Income / Expense

    color = Column(
        String(30),
        default="#2196F3",
    )

    icon = Column(
        String(50),
        default="wallet",
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    user = relationship(
        "User",
        back_populates="categories",
    )

    transactions = relationship(
        "Transaction",
        back_populates="category",
        cascade="all, delete",
    )

    budgets = relationship(
        "Budget",
        back_populates="category",
    )