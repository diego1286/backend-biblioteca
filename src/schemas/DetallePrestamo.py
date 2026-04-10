from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


# Base
class DetallePrestamoBase(BaseModel):
    id_prestamo: UUID
    id_ejemplar: UUID


# Crear
class DetallePrestamoCreate(DetallePrestamoBase):
    id_usuario_crea: Optional[UUID]


# Actualizar
class DetallePrestamoUpdate(BaseModel):
    id_usuario_edita: UUID


# Respuesta
class DetallePrestamoResponse(DetallePrestamoBase):
    id_detalle: UUID
    fecha_creacion: Optional[datetime]

    class Config:
        from_attributes = True
