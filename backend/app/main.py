from fastapi import FastAPI
from backend.app.api.v1.auth import router as auth_router
from backend.app.core.config import settings
from backend.app.database.db import Base, engine
from backend.app.api.v1.account import router as account_router
from backend.app.api.v1.category import router as category_router
from backend.app.api.v1.transaction import router as transaction_router
from backend.app.api.v1.budget import router as budget_router
from backend.app.api.v1.analytics import router as analytics_router
from backend.app.api.v1.copilot import router as copilot_router

import backend.app.models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)
app.include_router(auth_router)
app.include_router(account_router)
app.include_router(category_router)
app.include_router(transaction_router)
app.include_router(budget_router)
app.include_router(analytics_router)
app.include_router(copilot_router, prefix="/api/v1")


@app.get("/")
def home():

    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "database": "SQLite Connected"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }