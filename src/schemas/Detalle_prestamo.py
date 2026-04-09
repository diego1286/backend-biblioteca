from pydantic import BaseModel
from uuid import UUID

class DetallePrestamoBase(BaseModel):
    id_prestamo: UUID
    id_libro: UUID
    cantidad: int = 1

class DetallePrestamoCreate(DetallePrestamoBase):
    pass

class DetallePrestamoResponse(DetallePrestamoBase):
    id_detalle: UUID

    class Config:
        from_attributes = True