import uuid

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.database.config import Base


class Reserva(Base):

    __tablename__ = "reserva"

    id_reserva = Column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )

    id_usuario = Column(
        PG_UUID(as_uuid=True),
        ForeignKey("usuario.id_usuario"),
        nullable=False,
    )

    id_libro = Column(
        PG_UUID(as_uuid=True),
        ForeignKey("libro.id_libro"),
        nullable=False,
    )

    estado = Column(
        String(20),
        nullable=False,
        default="activa",
    )

    # Auditoría
    fecha_creacion = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    fecha_edicion = Column(
        DateTime(timezone=True),
        onupdate=func.now(),
    )

    id_usuario_crea = Column(
        PG_UUID(as_uuid=True),
        ForeignKey("usuario.id_usuario"),
        nullable=False,
    )

    id_usuario_edita = Column(
        PG_UUID(as_uuid=True),
        ForeignKey("usuario.id_usuario"),
        nullable=True,
    )

    # RELACIONES

    usuario = relationship(
        "Usuario", foreign_keys=[id_usuario], back_populates="reservas"
    )

    usuario_creador = relationship("Usuario", foreign_keys=[id_usuario_crea])

    usuario_editor = relationship("Usuario", foreign_keys=[id_usuario_edita])

    libro = relationship("Libro", back_populates="reservas")
