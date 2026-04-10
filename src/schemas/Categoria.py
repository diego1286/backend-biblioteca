from pydantic import BaseModel, Field, field_validator
from typing import Optional
from uuid import UUID
from datetime import datetime


class CategoriaBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    descripcion: Optional[str] = None

    @field_validator("nombre")
    @classmethod
    def limpiar_nombre(cls, value):
        return value.strip().title()


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None


class CategoriaResponse(CategoriaBase):
    id_categoria: UUID

    class Config:
        from_attributes = True
