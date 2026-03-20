"""
Entidad Libro
"""

import uuid

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.sql import func

from src.database.config import Base


class Libro(Base):
    __tablename__ = "libro"

    id_libro = Column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )

    titulo = Column(String(255), nullable=False)
    isbn = Column(String(50), nullable=False, unique=True)
    anio_publicacion = Column(Integer, nullable=False)

    # Trazabilidad
    id_usuario_crea = Column(
        PG_UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=True
    )

    id_usuario_edita = Column(
        PG_UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=True
    )

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())
