from fastapi import FastAPI
from backend.app.api.v1.auth import router as auth_router
from backend.app.core.config import settings
from backend.app.database.db import Base, engine

import backend.app.models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)
app.include_router(auth_router)

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