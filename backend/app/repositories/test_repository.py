from app.database.db import SessionLocal
from app.repositories.user_repository import UserRepository

db = SessionLocal()

user = UserRepository.get_by_email(
    db,
    "admin@example.com"
)

print(user)

db.close()
