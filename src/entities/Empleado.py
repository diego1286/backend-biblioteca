import uuid

from sqlalchemy import Column, String, Numeric, Date, DateTime, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.database.config import Base


class Empleado(Base):
    __tablename__ = "empleados"

    id_empleado = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )

    id_usuario = Column(
        UUID(as_uuid=True),
        ForeignKey("usuario.id_usuario"),
        nullable=False,
        unique=True,
    )

    cargo = Column(String(100), nullable=False)
    salario = Column(Numeric(10, 2), nullable=True)
    fecha_contratacion = Column(Date, nullable=False)
    tipo_contrato = Column(String(50), nullable=False)

    estado = Column(
        Enum("activo", "inactivo", "suspendido", name="estado_empleado"),
        default="activo",
        nullable=False,
    )

    # Auditoría
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())

    id_usuario_creacion = Column(
        UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=False
    )
    id_usuario_edita = Column(
        UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=True
    )

    # Relaciones
    usuario = relationship(
        "Usuario",
        foreign_keys=[id_usuario],
        back_populates="empleado",
    )

    usuario_creador = relationship(
        "Usuario",
        foreign_keys=[id_usuario_creacion],
    )

    usuario_editor = relationship(
        "Usuario",
        foreign_keys=[id_usuario_edita],
    )
