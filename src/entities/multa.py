import uuid
from sqlalchemy import Column, DateTime, ForeignKey, Numeric, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.database.config import Base


class Multa(Base):
    __tablename__ = "multa"

    id_multa = Column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )

    monto = Column(Numeric(10, 2), nullable=False)
    motivo = Column(String(255), nullable=False)

    # FK correcta
    id_prestamo = Column(
        PG_UUID(as_uuid=True), ForeignKey("prestamo.id_prestamo"), nullable=False
    )

    # Trazabilidad
    id_usuario_crea = Column(
        PG_UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=False
    )

    id_usuario_edita = Column(
        PG_UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=True
    )

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())

    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())

    # RELACIONES
    prestamo = relationship("Prestamo", back_populates="multas")
