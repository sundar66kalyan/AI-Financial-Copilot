from backend.app.database.db import SessionLocal
from backend.app.repositories.user_repository import UserRepository

db = SessionLocal()

user = UserRepository.get_by_email(
    db,
    "admin@example.com"
)

print(user)

db.close()