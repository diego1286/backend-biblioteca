from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from src.database.config import get_db
from src.schemas.Prestamo import (
    PrestamoCreate,
    PrestamoUpdate,
    PrestamoResponse,
)
from src.crud.Prestamo import *

router = APIRouter(prefix="/prestamos", tags=["Prestamos"])


@router.post("/", response_model=PrestamoResponse)
def crear(data: PrestamoCreate, db: Session = Depends(get_db)):
    return crear_prestamo(db, data)


@router.get("/", response_model=list[PrestamoResponse])
def listar(db: Session = Depends(get_db)):
    return obtener_prestamos(db)


@router.get("/{id_prestamo}", response_model=PrestamoResponse)
def obtener(id_prestamo: UUID, db: Session = Depends(get_db)):
    prestamo = obtener_prestamo_por_id(db, id_prestamo)

    if not prestamo:
        raise HTTPException(404, "Prestamo no encontrado")

    return prestamo


@router.put("/{id_prestamo}", response_model=PrestamoResponse)
def actualizar(id_prestamo: UUID, data: PrestamoUpdate, db: Session = Depends(get_db)):
    prestamo = actualizar_prestamo(db, id_prestamo, data)

    if not prestamo:
        raise HTTPException(404, "Prestamo no encontrado")

    return prestamo


@router.delete("/{id_prestamo}")
def eliminar(id_prestamo: UUID, db: Session = Depends(get_db)):
    success = eliminar_prestamo(db, id_prestamo)

    if not success:
        raise HTTPException(404, "Prestamo no encontrado")

    return {"message": "Prestamo eliminado"}
