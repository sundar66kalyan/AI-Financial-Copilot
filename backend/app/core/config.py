from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parents[3]

load_dotenv(BASE_DIR / ".env")


class Settings:
    APP_NAME = os.getenv("APP_NAME", "AI Financial Copilot")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
    DEBUG = os.getenv("DEBUG", "False")

    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8000"))

    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./financial_copilot.db")

    SECRET_KEY = os.getenv("SECRET_KEY", "change_this_secret_key")

    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60")
    )

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")


settings = Settings()