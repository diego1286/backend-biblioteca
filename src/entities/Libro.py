"""
Entidad Libro
"""

import uuid
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from src.database.config import Base


class Libro(Base):
    __tablename__ = "libro"

    id_libro = Column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )

    titulo = Column(String(255), nullable=False)
    isbn = Column(String(50), nullable=False, unique=True)
    anio_publicacion = Column(Integer, nullable=False)

    id_editorial = Column(
        PG_UUID(as_uuid=True), ForeignKey("editorial.id_editorial"), nullable=True
    )

    id_categoria = Column(
        PG_UUID(as_uuid=True), ForeignKey("categoria.id_categoria"), nullable=True
    )

    # Trazabilidad
    id_usuario_crea = Column(
        PG_UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=True
    )

    id_usuario_edita = Column(
        PG_UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=True
    )

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())

    # RELACIÓN MUCHOS A MUCHOS
    libro_autores = relationship("LibroAutor", back_populates="libro")
    autores = relationship("Autor", secondary="libro_autor", viewonly=True)
    categoria = relationship("Categoria", back_populates="libros")
    reservas = relationship("Reserva", back_populates="libro")
    editorial = relationship("Editorial", back_populates="libros")
