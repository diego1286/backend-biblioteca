import uuid
from sqlalchemy import Column, Numeric, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from database.config import Base

class Multa(Base):
    """
    Representa la tabla de multas en el sistema.
    """
    __tablename__ = "tbl_multas"

    id_multa = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )

    monto = Column(Numeric(10, 2), nullable=False)
    motivo = Column(String(255), nullable=False)
    id_prestamo = Column(UUID(as_uuid=True), ForeignKey("tbl_prestamos.id_prestamo"), nullable=False)