"""
Configuracion de la base de datos.

Usa DATABASE_URL desde variables de entorno y, si no existe,
cae a una base SQLite local para desarrollo.
"""

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DEFAULT_SQLITE_URL = "sqlite:///./biblioteca.db"
DATABASE_URL = os.getenv("DATABASE_URL", DEFAULT_SQLITE_URL)

connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args["check_same_thread"] = False
elif "neon.tech" in DATABASE_URL:
    connect_args["sslmode"] = "require"

engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
    pool_recycle=300,
    connect_args=connect_args,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """Generador de sesiones de base de datos."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    """Crear todas las tablas definidas en los modelos cargados."""
    Base.metadata.create_all(bind=engine)
