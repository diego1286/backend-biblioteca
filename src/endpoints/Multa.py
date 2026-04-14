from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.config import get_db
from src.schemas.Multa import MultaCreate, MultaResponse, MultaUpdate
from src.crud.Multa import (
    crear_multa,
    obtener_multas,
    obtener_multa,
    actualizar_multa,
    eliminar_multa,
)

router = APIRouter(prefix="/multas", tags=["Multas"])


@router.post("/", response_model=MultaResponse)
def crear(multa: MultaCreate, db: Session = Depends(get_db)):
    return crear_multa(db, multa)


@router.get("/", response_model=list[MultaResponse])
def listar(db: Session = Depends(get_db)):
    return obtener_multas(db)


@router.get("/{id_multa}", response_model=MultaResponse)
def obtener(id_multa: str, db: Session = Depends(get_db)):
    return obtener_multa(db, id_multa)


@router.put("/{id_multa}", response_model=MultaResponse)
def actualizar(id_multa: str, datos: MultaUpdate, db: Session = Depends(get_db)):
    return actualizar_multa(db, id_multa, datos)


@router.delete("/{id_multa}")
def eliminar(id_multa: str, db: Session = Depends(get_db)):
    return eliminar_multa(db, id_multa)
