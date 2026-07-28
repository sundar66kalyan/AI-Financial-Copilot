from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from backend.app.database.db import Base


class Budget(Base):
    __tablename__ = "budgets"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    name = Column(
        String(100),
        nullable=False,
    )

    amount = Column(
        Float,
        nullable=False,
    )

    month = Column(
        String(20),
        nullable=False,
    )

    year = Column(
        Integer,
        nullable=False,
    )

    is_active = Column(
        Boolean,
        default=True,
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

    category = relationship(
        "Category",
        back_populates="budgets",
    )

    user = relationship(
        "User",
        back_populates="budgets",
    )