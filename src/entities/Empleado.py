"""
Modelo de Empleado.

Extiende la información de un Usuario dentro del sistema,
incluyendo datos laborales y de auditoría.
"""

import uuid

from sqlalchemy import Column, Date, DateTime, Enum, ForeignKey, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database.config import Base


class Empleado(Base):
    """
    Representa un empleado del sistema.

    Está vinculado a un usuario existente y contiene
    información adicional laboral.
    """

    __tablename__ = "tbl_empleados"

    id_empleado = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
        doc="Identificador único del empleado.",
    )

    id_usuario = Column(
        UUID(as_uuid=True),
        ForeignKey("tbl_usuarios.id_usuario"),
        nullable=False,
        unique=True,
        doc="ID del usuario asociado al empleado.",
    )

    cargo = Column(
        String(100),
        nullable=False,
        doc="Cargo del empleado dentro de la organización.",
    )

    salario = Column(
        Numeric(10, 2),
        nullable=True,
        doc="Salario del empleado.",
    )

    fecha_contratacion = Column(
        Date,
        nullable=False,
        doc="Fecha en la que el empleado fue contratado.",
    )

    tipo_contrato = Column(
        String(50),
        nullable=False,
        doc="Tipo de contrato (indefinido, temporal, prestación de servicios, etc.).",
    )

    estado = Column(
        Enum("activo", "inactivo", "suspendido", name="estado_empleado"),
        default="activo",
        nullable=False,
        doc="Estado del empleado.",
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
        doc="Usuario que creó el registro.",
    )

    id_usuario_edita = Column(
        UUID(as_uuid=True),
        ForeignKey("tbl_usuarios.id_usuario"),
        nullable=True,
        doc="Usuario que realizó la última edición.",
    )

    # Relaciones

    usuario = relationship(
        "Usuario",
        foreign_keys=[id_usuario],
        backref="empleado",
        doc="Usuario asociado a este empleado.",
    )

    usuario_creador = relationship(
        "Usuario",
        foreign_keys=[id_usuario_creacion],
        doc="Usuario que creó el registro.",
    )

    usuario_editor = relationship(
        "Usuario",
        foreign_keys=[id_usuario_edita],
        doc="Usuario que editó el registro.",
    )

    def __repr__(self) -> str:
        """
        Representación en texto del empleado.

        Returns:
            str: Información básica del empleado.
        """
        return (
            f"<Empleado(id_empleado={self.id_empleado}, "
            f"cargo='{self.cargo}', estado='{self.estado}')>"
        )
