import uuid
from sqlalchemy import Column, DateTime, ForeignKey, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.config import Base

class Multa(Base):
    """
    Modelo de Multa con auditoría completa.
    """
    __tablename__ = "tbl_multas"

    id_multa = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    monto = Column(Numeric(10, 2), nullable=False)
    motivo = Column(String(255), nullable=False)
    id_prestamo = Column(UUID(as_uuid=True), ForeignKey("tbl_prestamos.id_prestamo"), nullable=False)

    # --- AUDITORÍA (LO QUE SUBE LA NOTA) ---
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())
    id_usuario_creacion = Column(UUID(as_uuid=True), ForeignKey("tbl_usuarios.id_usuario"), nullable=False)
    id_usuario_edita = Column(UUID(as_uuid=True), ForeignKey("tbl_usuarios.id_usuario"), nullable=True)

    # Relación con el creador
    usuario_creador = relationship("Usuario", foreign_keys=[id_usuario_creacion])

    def __repr__(self) -> str:
        return f"<Multa(monto={self.monto}, motivo='{self.motivo}')>"