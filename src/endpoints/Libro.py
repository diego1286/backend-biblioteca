from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from src.database.config import get_db
from src.schemas.Libro import LibroCreate, LibroUpdate, LibroResponse
from src.crud.Libro import (
    crear_libro,
    obtener_libros,
    obtener_libro_por_id,
    actualizar_libro,
    eliminar_libro,
)

router = APIRouter(prefix="/libros", tags=["Libros"])


@router.post("/", response_model=LibroResponse)
def crear(data: LibroCreate, db: Session = Depends(get_db)):
    try:
        return crear_libro(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[LibroResponse])
def listar(db: Session = Depends(get_db)):
    return obtener_libros(db)


@router.get("/{id_libro}", response_model=LibroResponse)
def obtener(id_libro: UUID, db: Session = Depends(get_db)):
    libro = obtener_libro_por_id(db, id_libro)

    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")

    return libro


@router.put("/{id_libro}", response_model=LibroResponse)
def actualizar(id_libro: UUID, data: LibroUpdate, db: Session = Depends(get_db)):
    try:
        libro = actualizar_libro(db, id_libro, data)

        if not libro:
            raise HTTPException(status_code=404, detail="Libro no encontrado")

        return libro

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{id_libro}")
def eliminar(id_libro: UUID, db: Session = Depends(get_db)):
    success = eliminar_libro(db, id_libro)

    if not success:
        raise HTTPException(status_code=404, detail="Libro no encontrado")

    return {"message": "Libro eliminado"}
