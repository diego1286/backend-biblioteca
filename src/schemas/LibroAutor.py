from pydantic import BaseModel
from uuid import UUID


class LibroAutorCreate(BaseModel):
    id_libro: UUID
    id_autor: UUID


class LibroAutorResponse(LibroAutorCreate):
    class Config:
        from_attributes = True
