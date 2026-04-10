from pydantic import BaseModel, Field, field_validator
from typing import Optional
from uuid import UUID
from datetime import datetime


# Clase base de usuario
class UsuarioBase(BaseModel):
    nombre_usuario: str = Field(..., min_length=1, max_length=150)
    rol: str = Field(..., min_length=1, max_length=50)
    activo: bool = True

    @field_validator("nombre_usuario", "rol")
    @classmethod
    def limpiar_texto(cls, value):
        return value.strip().title()


# crear usuario
class UsuarioCreate(UsuarioBase):
    contrasena: str = Field(..., min_length=6)

    @field_validator("contrasena")
    @classmethod
    def limpiar_password(cls, value):
        return value.strip()


# Actualizar usuario
class UsuarioUpdate(BaseModel):
    nombre_usuario: Optional[str] = None
    rol: Optional[str] = None
    contrasena: Optional[str] = None
    activo: Optional[bool] = None


# Respuesta del schema
class UsuarioResponse(UsuarioBase):
    id_usuario: UUID
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime]

    class config:
        from_attributes = True
