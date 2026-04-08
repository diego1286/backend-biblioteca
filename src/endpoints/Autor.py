from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from src.database.config import get_db
from src.schemas.Autor import AutorCreate, AutorResponde, AutorUpdate
from src.crud.Autor import *

router = APIRouter(prefix="/autores", tags=["Autores"])


# crear un autor
@router.post("/", response_model=AutorResponde)
def crear(autor: AutorCreate, db: Session = Depends(get_db)):
    return crear_autor(db, autor)


# obtener autor
@router.get("/", response_model=list[AutorResponde])
def obtener(db: Session = Depends(get_db)):
    return obtener_autores(db)


# Obtener autor por ID
@router.get("/{id_autor}", response_model=AutorResponde)
def obtenerXiD(id_autor: UUID, db: Session = Depends(get_db)):
    autor = obtener_autor_por_id(db, id_autor)
    if not autor:
        raise HTTPException(404, "Autor no encontrado")
    return autor


# actualizar
@router.put("/{id_autor}", response_model=AutorResponde)
def actualizar(id_autor: UUID, data: AutorUpdate, db: Session = Depends(get_db)):
    autor = actualizar_autor(db, id_autor, data)
    if not autor:
        raise HTTPException(404, "Autor no encontrado")
    return autor


@router.delete("/{id_autor}")
def eliminar_autor(id_autor: UUID, db: Session = Depends(get_db)):
    succes = eliminar_autor(db, id_autor)
    if not succes:
        raise HTTPException(404, "Autor no encnotrado")
    return {"message": "Autor eliminado"}
