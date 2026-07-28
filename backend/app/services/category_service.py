from sqlalchemy.orm import Session

from backend.app.repositories.category_repository import CategoryRepository
from backend.app.schemas.category import CategoryCreate


class CategoryService:

    @staticmethod
    def create_category(
        db: Session,
        category: CategoryCreate,
        user_id: int,
    ):
        return CategoryRepository.create(
            db,
            category,
            user_id,
        )

    @staticmethod
    def get_categories(
        db: Session,
        user_id: int,
    ):
        return CategoryRepository.get_all(
            db,
            user_id,
        )