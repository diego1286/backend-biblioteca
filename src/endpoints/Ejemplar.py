from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from src.database.config import get_db
from src.schemas.Ejemplar import CreateEjemplar, updateEjemplar, EjemplarResponse
from src.crud.Ejemplar import *


router = APIRouter(prefix="/ejemplares", tags=["Ejemplares"])


@router.post("/", response_model=EjemplarResponse)
def crear(data: CreateEjemplar, db: Session = Depends(get_db)):
    try:
        return crear_Ejemplar(db, data)
    except ValueError as e:
        raise HTTPException(400, str(e))


@router.get("/", response_model=list[EjemplarResponse])
def listar(db: Session = Depends(get_db)):
    return obtener_ejemplares(db)


@router.get("/{id_ejemplar}", response_model=EjemplarResponse)
def obtener(id_ejemplar: UUID, db: Session = Depends(get_db)):
    ejemplar = obtener_ejemplar_por_id(db, id_ejemplar)

    if not ejemplar:
        raise HTTPException(404, "Ejemplar no encontrado")

    return ejemplar


@router.put("/{id_ejemplar}", response_model=EjemplarResponse)
def actualizar(id_ejemplar: UUID, data: updateEjemplar, db: Session = Depends(get_db)):
    try:
        ejemplar = actualizar_ejemplar(db, id_ejemplar, data)

        if not ejemplar:
            raise HTTPException(404, "Ejemplar no encontrado")

        return ejemplar

    except ValueError as e:
        raise HTTPException(400, str(e))


@router.delete("/{id_ejemplar}")
def eliminar(id_ejemplar: UUID, db: Session = Depends(get_db)):
    success = eliminar_ejemplar(db, id_ejemplar)

    if not success:
        raise HTTPException(404, "Ejemplar no encontrado")

    return {"message": "Ejemplar eliminado"}
