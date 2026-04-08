from pydantic import BaseModel, Field, field_validator
from typing import Optional
from uuid import UUID
from datetime import datetime


# clase base
class LibroBase(BaseModel):
    titulo: str = Field(..., min_length=2, max_length=30)
    isbn: str = Field(..., min_length=2, max_length=30)
    anio_publicacion: int

    @field_validator("titulo", "isbn")
    @classmethod
    def limpiar_text0(cls, value):
        return value.strip()


# crear
class createLibro(LibroBase):
    id_usuario_crea: Optional[UUID]


# actualizar
class updateLibro(BaseModel):
    titulo: Optional[str] = None
    isbn: Optional[str] = None
    anio_publicacion: Optional[int] = None
    id_usuario_edita: UUID


# Respuesta
class LibroResponse(LibroBase):
    id_libro: UUID
    fecha_creacion: Optional[datetime]

    class config:
        from_attributes = True
