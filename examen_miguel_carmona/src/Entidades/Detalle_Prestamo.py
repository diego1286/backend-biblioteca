import uuid
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database.config import Base

class DetallePrestamo(Base):
    __tablename__ = "tbl_detalles_prestamos"

    id_detalle = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    id_prestamo = Column(UUID(as_uuid=True), ForeignKey("tbl_prestamos.id_prestamo"), nullable=False)
    id_libro = Column(UUID(as_uuid=True), ForeignKey("tbl_libros.id_libro"), nullable=False)
    cantidad = Column(Integer, default=1, nullable=False)

    # Relación con la tabla Prestamo
    prestamo = relationship("Prestamo", back_populates="detalles")

    def __repr__(self) -> str:
        return f"<DetallePrestamo(id={self.id_detalle}, libro={self.id_libro})>"