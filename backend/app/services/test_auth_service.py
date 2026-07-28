from app.database.db import SessionLocal
from app.schemas.user import UserCreate
from app.services.auth_service import AuthService

db = SessionLocal()

user = UserCreate(
    username="admin",
    email="admin@example.com",
    password="Financial@123"
)

try:
    created_user = AuthService.register(db, user)

    print("User Created Successfully")
    print(created_user.username)
    print(created_user.email)

except Exception as ex:
    print(ex)

finally:
    db.close()
