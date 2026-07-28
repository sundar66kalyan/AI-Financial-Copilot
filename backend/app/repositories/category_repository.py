from sqlalchemy.orm import Session

from backend.app.models.category import Category
from backend.app.schemas.category import CategoryCreate


class CategoryRepository:

    @staticmethod
    def create(
        db: Session,
        category: CategoryCreate,
        user_id: int,
    ):

        db_category = Category(
            name=category.name,
            category_type=category.category_type,
            color=category.color,
            icon=category.icon,
            user_id=user_id,
        )

        db.add(db_category)
        db.commit()
        db.refresh(db_category)

        return db_category

    @staticmethod
    def get_all(
        db: Session,
        user_id: int,
    ):
        return (
            db.query(Category)
            .filter(Category.user_id == user_id)
            .all()
        )