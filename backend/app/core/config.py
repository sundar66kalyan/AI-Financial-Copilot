from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parents[3]

load_dotenv(BASE_DIR / ".env")


class Settings:
    APP_NAME = os.getenv("APP_NAME")
    APP_VERSION = os.getenv("APP_VERSION")
    DEBUG = os.getenv("DEBUG")

    HOST = os.getenv("HOST")
    PORT = int(os.getenv("PORT"))

    DATABASE_URL = os.getenv("DATABASE_URL")

    SECRET_KEY = os.getenv("SECRET_KEY")

    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    )

    LOG_LEVEL = os.getenv("LOG_LEVEL")

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


settings = Settings()