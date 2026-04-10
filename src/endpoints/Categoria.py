from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from src.database.config import get_db
from src.schemas.Categoria import (
    CategoriaCreate,
    CategoriaUpdate,
    CategoriaResponse,
)
from src.crud.Categoria import *

router = APIRouter(prefix="/categorias", tags=["Categorias"])


@router.post("/", response_model=CategoriaResponse)
def crear(data: CategoriaCreate, db: Session = Depends(get_db)):
    try:
        return crear_categoria(db, data)
    except ValueError as e:
        raise HTTPException(400, str(e))


@router.get("/", response_model=list[CategoriaResponse])
def listar(db: Session = Depends(get_db)):
    return obtener_categorias(db)


@router.get("/{id_categoria}", response_model=CategoriaResponse)
def obtener(id_categoria: UUID, db: Session = Depends(get_db)):
    categoria = obtener_categoria_por_id(db, id_categoria)

    if not categoria:
        raise HTTPException(404, "Categoría no encontrada")

    return categoria


@router.put("/{id_categoria}", response_model=CategoriaResponse)
def actualizar(
    id_categoria: UUID, data: CategoriaUpdate, db: Session = Depends(get_db)
):
    try:
        categoria = actualizar_categoria(db, id_categoria, data)

        if not categoria:
            raise HTTPException(404, "Categoría no encontrada")

        return categoria

    except ValueError as e:
        raise HTTPException(400, str(e))


@router.delete("/{id_categoria}")
def eliminar(id_categoria: UUID, db: Session = Depends(get_db)):
    success = eliminar_categoria(db, id_categoria)

    if not success:
        raise HTTPException(404, "Categoría no encontrada")

    return {"message": "Categoría eliminada"}
