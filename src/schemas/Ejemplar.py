from pydantic import BaseModel, Field, field_validator
from typing import Optional
from uuid import UUID
from datetime import datetime


# clase base
class EjemplarBase(BaseModel):
    id_libro: UUID
    codigo_barra: str = Field(..., min_length=3, max_length=30)
    estado: str = Field(..., min_length=3, max_length=50)
    ubicacion: str = Field(..., min_length=2, max_length=100)

    @field_validator("codigo_barra", "estado", "ubicacion")
    @classmethod
    def limpiar_texto(cls, value):
        return value.strip()


# crearEjemplar
class CreateEjemplar(EjemplarBase):
    id_usuario_crea: Optional[UUID]


# actualizar ejemplar
class updateEjemplar(BaseModel):
    id_libro: Optional[UUID] = None
    codigo_barra: Optional[str] = None
    estado: Optional[str] = None
    ubicacion: Optional[str] = None
    id_usuario_edita: UUID


# Clase respuesta
class EjemplarResponse(EjemplarBase):
    id_ejemplar: UUID
    fecha_creacion: Optional[datetime]

    class config:
        from_attributes = True
