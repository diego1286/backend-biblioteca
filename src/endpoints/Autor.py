from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from src.database.config import get_db
from src.schemas.Autor import AutorCreate, AutorResponse, AutorUpdate
from src.crud.Autor import (
    crear_autor,
    obtener_autores,
    obtener_autor_por_id,
    actualizar_autor,
    eliminar_autor,
)

router = APIRouter(prefix="/autores", tags=["Autores"])


@router.post("/", response_model=AutorResponse)
def crear(autor: AutorCreate, db: Session = Depends(get_db)):
    return crear_autor(db, autor)


@router.get("/", response_model=list[AutorResponse])
def listar(db: Session = Depends(get_db)):
    return obtener_autores(db)


@router.get("/{id_autor}", response_model=AutorResponse)
def obtener_por_id(id_autor: UUID, db: Session = Depends(get_db)):
    autor = obtener_autor_por_id(db, id_autor)

    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")

    return autor


@router.put("/{id_autor}", response_model=AutorResponse)
def actualizar(id_autor: UUID, data: AutorUpdate, db: Session = Depends(get_db)):
    autor = actualizar_autor(db, id_autor, data)

    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")

    return autor


@router.delete("/{id_autor}")
def eliminar(id_autor: UUID, db: Session = Depends(get_db)):
    success = eliminar_autor(db, id_autor)

    if not success:
        raise HTTPException(status_code=404, detail="Autor no encontrado")

    return {"message": "Autor eliminado"}
