from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal
from typing import Optional


class MultaBase(BaseModel):
    monto: Decimal
    motivo: str
    id_prestamo: UUID


class MultaCreate(MultaBase):
    id_usuario_crea: UUID


class MultaUpdate(BaseModel):
    monto: Optional[Decimal] = None
    motivo: Optional[str] = None


class MultaResponse(MultaBase):
    id_multa: UUID

    class Config:
        from_attributes = True
