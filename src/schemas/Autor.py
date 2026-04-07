from pydantic import BaseModel, Field, field_validator
from uuid import UUID
from typing import Optional
from datetime import datetime


# Crear autor
class AutoBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    apellido: str = Field(..., min_length=2, max_length=100)
    nacionalidad: str = Field(..., min_length=2, max_length=100)
    id_usuario_crea: Optional[UUID]

    @field_validator("nombre", "apellido", "nacionalidad")
    @classmethod
    def limpiar_texto(cls, value):
        return value.strip().title()


class AutorCreate(AutoBase):
    id_usuario_crea: Optional[UUID]


class AutorUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    nacionalidad: Optional[str] = None
    id_usuario_edita: UUID


class AutorResponde(AutoBase):
    id_autor: UUID
    fecha_creacion: Optional[datetime]

    class Config:
        from_attributes = True
