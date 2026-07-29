from sqlalchemy.orm import Session

from app.auth.jwt_handler import create_access_token
from app.auth.password import hash_password, verify_password
from app.repositories.user_repository import UserRepository
from app.schemas.token import Token
from app.schemas.user import UserCreate, UserLogin


class AuthService:

    @staticmethod
    def register(db: Session, user: UserCreate):

        if UserRepository.get_by_email(db, user.email):
            raise ValueError("Email already registered.")

        if UserRepository.get_by_username(db, user.username):
            raise ValueError("Username already exists.")

        hashed_password = hash_password(user.password)

        return UserRepository.create_user(
            db=db,
            user=user,
            hashed_password=hashed_password,
        )

    @staticmethod
    def login(db: Session, credentials: UserLogin) -> Token:

        print("=" * 60)
        print("LOGIN EMAIL:", credentials.email)

        db_user = UserRepository.get_by_email(db, credentials.email)

        print("DB USER:", db_user)

        if db_user:
            print("DB EMAIL:", db_user.email)
            print("PASSWORD MATCH:", verify_password(credentials.password, db_user.password))
        print("=" * 60)

        if db_user is None:
            raise ValueError("Invalid email or password.")

        if not verify_password(credentials.password, db_user.password):
            raise ValueError("Invalid email or password.")

        access_token = create_access_token({"sub": db_user.email})

        return Token(
            access_token=access_token,
            token_type="bearer",
        )