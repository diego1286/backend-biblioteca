import uuid
from sqlalchemy import Column, DateTime, ForeignKey, String, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.config import Base

class Prestamo(Base):
    __tablename__ = "tbl_prestamos"

    id_prestamo = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    id_usuario = Column(UUID(as_uuid=True), ForeignKey("tbl_usuarios.id_usuario"), nullable=False)
    fecha_prestamo = Column(Date, server_default=func.current_date(), nullable=False)
    fecha_devolucion_prevista = Column(Date, nullable=False)
    fecha_devolucion_real = Column(Date, nullable=True)
    estado = Column(String(20), default="activo")

    # --- AUDITORÍA ---
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())
    id_usuario_creacion = Column(UUID(as_uuid=True), ForeignKey("tbl_usuarios.id_usuario"), nullable=False)
    id_usuario_edita = Column(UUID(as_uuid=True), ForeignKey("tbl_usuarios.id_usuario"), nullable=True)

    # Relación con Usuario
    usuario = relationship("Usuario", foreign_keys=[id_usuario], backref="prestamos")

    def __repr__(self) -> str:
        return f"<Prestamo(id={self.id_prestamo}, estado='{self.estado}')>"