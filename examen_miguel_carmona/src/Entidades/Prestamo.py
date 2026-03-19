import uuid
from sqlalchemy import Column, ForeignKey, Date, String
from sqlalchemy.dialects.postgresql import UUID
from database.config import Base

class Prestamo(Base):
    __tablename__ = "tbl_prestamos"

    id_prestamo = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    id_usuario = Column(UUID(as_uuid=True), ForeignKey("tbl_usuarios.id_usuario"), nullable=False)
    fecha_prestamo = Column(Date, nullable=False)
    estado = Column(String(20), default="activo")