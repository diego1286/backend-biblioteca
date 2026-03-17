"""
Modelo de Usuario con auditoría.

Este módulo define la entidad Usuario para la base de datos,
incluyendo campos de auditoría para control de creación y edición.
"""

import uuid

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database.config import Base


class Usuario(Base):
    """
    Representa la tabla de usuarios en la base de datos.

    Incluye información básica del usuario y campos de auditoría
    para rastrear quién crea y modifica los registros.
    """

    __tablename__ = "tbl_usuarios"

    id_usuario = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
        doc="Identificador único del usuario (UUID).",
    )

    nombre = Column(
        String(100),
        nullable=False,
        doc="Nombre completo del usuario.",
    )

    nombre_usuario = Column(
        String(50),
        unique=True,
        index=True,
        nullable=False,
        doc="Nombre de usuario único.",
    )

    email = Column(
        String(150),
        unique=True,
        index=True,
        nullable=False,
        doc="Correo electrónico del usuario.",
    )

    contrasena_hash = Column(
        String(255),
        nullable=False,
        doc="Contraseña del usuario en formato hash.",
    )

    telefono = Column(
        String(20),
        nullable=True,
        doc="Número de teléfono del usuario.",
    )

    activo = Column(
        Boolean,
        default=True,
        doc="Indica si el usuario está activo.",
    )

    es_admin = Column(
        Boolean,
        default=False,
        doc="Indica si el usuario tiene privilegios de administrador.",
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
        doc="ID del usuario que creó el registro.",
    )

    id_usuario_edita = Column(
        UUID(as_uuid=True),
        ForeignKey("tbl_usuarios.id_usuario"),
        nullable=True,
        doc="ID del usuario que realizó la última edición.",
    )

    # Relaciones

    usuario_creador = relationship(
        "Usuario",
        foreign_keys=[id_usuario_creacion],
        backref="usuarios_creados",
        doc="Relación al usuario que creó este registro.",
    )

    usuario_editor = relationship(
        "Usuario",
        foreign_keys=[id_usuario_edita],
        backref="usuarios_editados",
        doc="Relación al usuario que editó este registro.",
    )

    def __repr__(self) -> str:
        """
        Returns:
            str: Cadena representativa del usuario.
        """
        return (
            f"<Usuario(id_usuario={self.id_usuario}, "
            f"nombre='{self.nombre}', email='{self.email}')>"
        )
