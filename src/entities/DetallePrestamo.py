import uuid

from sqlalchemy import Column, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from src.database.config import Base


class DetallePrestamo(Base):
    __tablename__ = "detalle_prestamo"

    id_detalle = Column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )

    id_prestamo = Column(
        PG_UUID(as_uuid=True),
        ForeignKey("prestamo.id_prestamo"),
        nullable=False,
    )

    id_ejemplar = Column(
        PG_UUID(as_uuid=True),
        ForeignKey("ejemplar.id_ejemplar"),
        nullable=False,
    )

    # Trazabilidad
    id_usuario_crea = Column(
        PG_UUID(as_uuid=True),
        ForeignKey("usuario.id_usuario"),
        nullable=True,
    )

    id_usuario_edita = Column(
        PG_UUID(as_uuid=True),
        ForeignKey("usuario.id_usuario"),
        nullable=True,
    )

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())

    # RELACIONES
    prestamo = relationship("Prestamo")
    ejemplar = relationship("Ejemplar")
