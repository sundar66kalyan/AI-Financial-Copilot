from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.database.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String(100),
        unique=True,
        nullable=False
    )

    email = Column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    password = Column(
        String(255),
        nullable=False
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    accounts = relationship(
        "Account",
        back_populates="user",
        cascade="all, delete",
    )

    categories = relationship(
        "Category",
        back_populates="user",
        cascade="all, delete",
    )

    transactions = relationship(
        "Transaction",
        back_populates="user",
        cascade="all, delete",
    )

    budgets = relationship(
        "Budget",
        back_populates="user",
        cascade="all, delete",
    )
