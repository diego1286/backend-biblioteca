"""
Entidad LibroAutor (tabla intermedia)
"""

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from src.database.config import Base


class LibroAutor(Base):
    __tablename__ = "libro_autor"

    id_libro = Column(
        PG_UUID(as_uuid=True), ForeignKey("libro.id_libro"), primary_key=True
    )

    id_autor = Column(
        PG_UUID(as_uuid=True), ForeignKey("autor.id_autor"), primary_key=True
    )
