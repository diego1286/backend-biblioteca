from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class EditorialBase(BaseModel):
    nombre: str
    pais: str


class EditorialCreate(EditorialBase):
    pass


class EditorialUpdate(BaseModel):
    nombre: Optional[str] = None
    pais: Optional[str] = None


class EditorialResponse(EditorialBase):
    id_editorial: UUID

    class Config:
        from_attributes = True
