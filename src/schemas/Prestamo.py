from pydantic import BaseModel, Field, field_validator
from typing import Optional
from uuid import UUID
from datetime import date, datetime


class PrestamoBase(BaseModel):
    id_usuario: UUID
    fecha_prestamo: date
    fecha_devolucion_estimada: date
    estado: str = Field(..., min_length=3, max_length=50)

    @field_validator("estado")
    @classmethod
    def limpiar_estado(cls, value):
        return value.strip().lower()


class PrestamoCreate(PrestamoBase):
    id_usuario_crea: Optional[UUID]

    @field_validator("fecha_devolucion_estimada")
    @classmethod
    def validar_fechas(cls, value, values):
        if "fecha_prestamo" in values and value < values["fecha_prestamo"]:
            raise ValueError(
                "La fecha estimada no puede ser menor a la fecha de préstamo"
            )
        return value


class PrestamoUpdate(BaseModel):
    fecha_devolucion_real: Optional[date] = None
    estado: Optional[str] = None
    id_usuario_edita: UUID


class PrestamoResponse(PrestamoBase):
    id_prestamo: UUID
    fecha_devolucion_real: Optional[date]
    fecha_creacion: Optional[datetime]

    class Config:
        from_attributes = True
