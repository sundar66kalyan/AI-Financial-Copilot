from fastapi import FastAPI
from app.api.v1.auth import router as auth_router
from app.core.config import settings
from app.database.db import Base, engine
from app.api.v1.account import router as account_router
from app.api.v1.category import router as category_router
from app.api.v1.transaction import router as transaction_router
from app.api.v1.budget import router as budget_router
from app.api.v1.analytics import router as analytics_router
from app.api.v1.copilot import router as copilot_router
from app.api.v1.investment import router as investment_router
from app.api.v1.report import router as report_router
from app.api.v1.insights import router as insights_router

import app.models

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
app.include_router(investment_router)
app.include_router(report_router)
app.include_router(insights_router)

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