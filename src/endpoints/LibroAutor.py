from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from src.database.config import get_db
from src.schemas.LibroAutor import LibroAutorCreate
from src.crud.LibroAutor import asignar_autor_a_libro, eliminar_autor_de_libro

router = APIRouter(prefix="/libro-autor", tags=["Libro-Autor"])


@router.post("/")
def asignar(data: LibroAutorCreate, db: Session = Depends(get_db)):
    return asignar_autor_a_libro(db, data.id_libro, data.id_autor)


@router.delete("/{id_libro}/{id_autor}")
def eliminar(id_libro: UUID, id_autor: UUID, db: Session = Depends(get_db)):

    success = eliminar_autor_de_libro(db, id_libro, id_autor)

    if not success:
        raise HTTPException(status_code=404, detail="Relación no encontrada")

    return {"message": "Relación eliminada"}
