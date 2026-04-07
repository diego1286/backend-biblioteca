import uvicorn
from fastapi import FastAPI

from src.api.routers import api_router
from src.database import models  # noqa: F401
from src.database.config import DATABASE_URL, create_tables

app = FastAPI(
    title="Biblioteca API",
    description="API REST del sistema de biblioteca con FastAPI y SQLAlchemy.",
    version="1.0.0",
)

create_tables()

app.include_router(api_router, prefix="/api")


def get_database_engine_name() -> str:
    if DATABASE_URL.startswith("sqlite"):
        return "sqlite"
    if "postgresql" in DATABASE_URL:
        return "postgresql"
    return "database_configured"


@app.get("/", tags=["Inicio"])
def root():
    return {
        "message": "Biblioteca API en ejecucion",
        "database_engine": get_database_engine_name(),
        "docs": "/docs",
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
