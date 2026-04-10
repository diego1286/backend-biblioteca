from pydantic import BaseModel, Field, field_validator
from typing import Optional
from uuid import UUID
from datetime import datetime


class LibroBase(BaseModel):
    titulo: str = Field(..., min_length=2, max_length=255)
    isbn: str = Field(..., min_length=5, max_length=50)
    anio_publicacion: int

    @field_validator("titulo", "isbn")
    @classmethod
    def limpiar_texto(cls, value):
        return value.strip()

    @field_validator("anio_publicacion")
    @classmethod
    def validar_anio(cls, value):
        if value <= 0:
            raise ValueError("Año inválido")
        return value


class LibroCreate(LibroBase):
    id_usuario_crea: Optional[UUID]


class LibroUpdate(BaseModel):
    titulo: Optional[str] = None
    isbn: Optional[str] = None
    anio_publicacion: Optional[int] = None
    id_usuario_edita: UUID


class LibroResponse(LibroBase):
    id_libro: UUID
    fecha_creacion: Optional[datetime]

    class Config:
        from_attributes = True
