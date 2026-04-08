from pydantic import BaseModel, Field, field_validator
from typing import Optional
from uuid import UUID
from datetime import date, datetime


# clase Base
class PrestamoBase(BaseModel):
    id_usuario: UUID
    fecha_prestamo: date
    fecha_devolucion_estimada: date
    estado: str = Field(..., min_length=3, max_length=50)

    @field_validator("estado")
    @classmethod
    def limpiar_estado(cls, value):
        return value.strip().lower()


#  Crear
class PrestamoCreate(PrestamoBase):
    id_usuario_crea: Optional[UUID]


#  Actualizar
class PrestamoUpdate(BaseModel):
    fecha_devolucion_real: Optional[date] = None
    estado: Optional[str] = None
    id_usuario_edita: UUID


#  Respuesta
class PrestamoResponse(PrestamoBase):
    id_prestamo: UUID
    fecha_devolucion_real: Optional[date]
    fecha_creacion: Optional[datetime]

    class Config:
        from_attributes = True
