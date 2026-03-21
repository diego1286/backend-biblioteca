"""
Modelo de Categoria
"""
import uuid
from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.postgresql import UUID
from src.database.config import Base

class Categoria(Base):
    __tablename__ = "tbl_categorias"
    id_categoria = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    nombre = Column(
        String(100),
        nullable=False,
        unique=True,
    )
    descripcion = Column(
        Text,
        nullable=True,
    )
    def __repr__(self):
        return f"<Categoria(id_categoria={self.id_categoria}, nombre='{self.nombre}')>"