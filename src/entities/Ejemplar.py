"""
Entidad Ejemplar
"""

import uuid

from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.sql import func

from src.database.config import Base


class Ejemplar(Base):
    __tablename__ = "ejemplar"

    id_ejemplar = Column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )

    id_libro = Column(
        PG_UUID(as_uuid=True), ForeignKey("libro.id_libro"), nullable=False
    )

    codigo_barra = Column(String(100), nullable=False, unique=True)
    estado = Column(String(50), nullable=False)
    ubicacion = Column(String(100), nullable=False)

    # Trazabilidad
    id_usuario_crea = Column(
        PG_UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=True
    )

    id_usuario_edita = Column(
        PG_UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=True
    )

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())
