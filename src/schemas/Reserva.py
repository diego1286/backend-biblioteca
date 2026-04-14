from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class ReservaBase(BaseModel):
    id_usuario: UUID
    id_libro: UUID
    estado: str = "activa"


class ReservaCreate(ReservaBase):
    id_usuario_crea: UUID


class ReservaUpdate(BaseModel):
    estado: Optional[str] = None


class ReservaResponse(ReservaBase):
    id_reserva: UUID

    class Config:
        from_attributes = True
