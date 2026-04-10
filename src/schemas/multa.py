from pydantic import BaseModel, Field, field_validator
from typing import Optional
from uuid import UUID
from datetime import datetime
from decimal import Decimal

class MultaBase(BaseModel):
    id_prestamo: UUID
    monto: Decimal
    motivo: str = Field(..., min_length=3, max_length=255)

    @field_validator("motivo")
    @classmethod
    def limpiar_motivo(cls, value):
        return value.strip()

class MultaCreate(MultaBase):
    id_usuario_creacion: UUID

class MultaUpdate(BaseModel):
    monto: Optional[Decimal] = None
    motivo: Optional[str] = None
    id_usuario_edita: UUID

class MultaResponse(MultaBase):
    id_multa: UUID
    fecha_creacion: datetime
    id_usuario_creacion: UUID

    class Config:
        from_attributes = True