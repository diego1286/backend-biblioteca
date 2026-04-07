"""
Entidad Prestamo
"""

import uuid

from sqlalchemy import Column, Date, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.sql import func

from src.database.config import Base


class Prestamo(Base):
    __tablename__ = "prestamo"

    id_prestamo = Column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )

    id_usuario = Column(
        PG_UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=False
    )

    id_empleado = Column(
        PG_UUID(as_uuid=True), ForeignKey("empleados.id_empleado"), nullable=False
    )

    fecha_prestamo = Column(Date, nullable=False)
    fecha_devolucion_estimada = Column(Date, nullable=False)
    fecha_devolucion_real = Column(Date, nullable=True)

    estado = Column(String(50), nullable=False)

    # Trazabilidad
    id_usuario_crea = Column(
        PG_UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=True
    )

    id_usuario_edita = Column(
        PG_UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=True
    )

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())
