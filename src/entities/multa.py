import uuid
from sqlalchemy import Column, DateTime, ForeignKey, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from src.database.config import Base

class Multa(Base):
    __tablename__ = "multa"

    id_multa = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    monto = Column(Numeric(10, 2), nullable=False)
    motivo = Column(String(255), nullable=False)
    
    # Referencia a la tabla de prestamos (Ajustado al estándar de Diego)
    id_prestamo = Column(UUID(as_uuid=True), ForeignKey("prestamo.id_prestamo"), nullable=False)

    # --- AUDITORÍA ---
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())
    id_usuario_creacion = Column(UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=False)
    id_usuario_edita = Column(UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=True)

    def __repr__(self) -> str:
        return f"<Multa(monto={self.monto}, motivo='{self.motivo}')>"