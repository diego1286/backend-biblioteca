import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import relationship

from src.database.config import Base


class Editorial(Base):

    __tablename__ = "editorial"

    id_editorial = Column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )

    nombre = Column(
        String(150),
        nullable=False,
        unique=True,
    )

    pais = Column(
        String(100),
        nullable=False,
    )

    # RELACIÓN
    libros = relationship("Libro", back_populates="editorial", cascade="all, delete")

    def __repr__(self):
        return f"<Editorial(id_editorial={self.id_editorial}, nombre='{self.nombre}')>"
