"""
Modelo de Reserva.

Define la entidad Reserva, que relaciona usuarios con libros.
Incluye auditoría para control de creación y edición.
"""

import uuid

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database.config import Base


class Reserva(Base):
    """
    Representa una reserva de un libro realizada por un usuario.
    """

    __tablename__ = "tbl_reservas"

    id_reserva = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
        doc="Identificador único de la reserva.",
    )

    id_usuario = Column(
        UUID(as_uuid=True),
        ForeignKey("tbl_usuarios.id_usuario"),
        nullable=False,
        doc="ID del usuario que realiza la reserva.",
    )

    id_libro = Column(
        UUID(as_uuid=True),
        ForeignKey("tbl_libros.id_libro"),
        nullable=False,
        doc="ID del libro reservado.",
    )

    estado = Column(
        String(20),
        nullable=False,
        default="activa",
        doc="Estado de la reserva: activa, cancelada o completada.",
    )

    # Auditoría

    fecha_creacion = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
        doc="Fecha de creación del registro.",
    )

    fecha_edicion = Column(
        DateTime(timezone=True),
        onupdate=func.now(),
        doc="Fecha de última edición del registro.",
    )

    id_usuario_creacion = Column(
        UUID(as_uuid=True),
        ForeignKey("tbl_usuarios.id_usuario"),
        nullable=False,
        doc="Usuario que creó la reserva.",
    )

    id_usuario_edita = Column(
        UUID(as_uuid=True),
        ForeignKey("tbl_usuarios.id_usuario"),
        nullable=True,
        doc="Usuario que editó la reserva.",
    )

    # Relaciones

    usuario = relationship(
        "Usuario",
        foreign_keys=[id_usuario],
        backref="reservas",
        doc="Usuario que realizó la reserva.",
    )

    libro = relationship(
        "Libro",
        backref="reservas",
        doc="Libro asociado a la reserva.",
    )

    usuario_creador = relationship(
        "Usuario",
        foreign_keys=[id_usuario_creacion],
        doc="Usuario que creó la reserva.",
    )

    usuario_editor = relationship(
        "Usuario",
        foreign_keys=[id_usuario_edita],
        doc="Usuario que editó la reserva.",
    )

    def __repr__(self) -> str:
        """
        Representación en texto de la reserva.

        Returns:
            str: Información básica de la reserva.
        """
        return f"<Reserva(id_reserva={self.id_reserva}, " f"estado='{self.estado}')>"
