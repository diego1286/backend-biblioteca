from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from src.database.config import get_db
# Importamos desde tus carpetas reales (fíjate en las minúsculas)
from src.schemas.multa import MultaCreate, MultaUpdate, MultaResponse
from src.crud.multa import *

router = APIRouter(prefix="/multas", tags=["Multas"])

@router.post("/", response_model=MultaResponse)
def crear(data: MultaCreate, db: Session = Depends(get_db)):
    return crear_multa(db, data)

@router.get("/", response_model=list[MultaResponse])
def listar(db: Session = Depends(get_db)):
    return obtener_multas(db)

@router.get("/{id_multa}", response_model=MultaResponse)
def obtener(id_multa: UUID, db: Session = Depends(get_db)):
    multa = obtener_multa_por_id(db, id_multa)
    if not multa:
        raise HTTPException(404, "Multa no encontrada")
    return multa

@router.put("/{id_multa}", response_model=MultaResponse)
def actualizar(id_multa: UUID, data: MultaUpdate, db: Session = Depends(get_db)):
    multa = actualizar_multa(db, id_multa, data)
    if not multa:
        raise HTTPException(404, "Multa no encontrada")
    return multa

@router.delete("/{id_multa}")
def eliminar(id_multa: UUID, db: Session = Depends(get_db)):
    if not eliminar_multa(db, id_multa):
        raise HTTPException(404, "Multa no encontrada")
    return {"message": "Multa eliminada"}