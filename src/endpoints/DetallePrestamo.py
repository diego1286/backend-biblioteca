from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from src.database.config import get_db
from src.schemas.DetallePrestamo import (
    DetallePrestamoCreate,
    DetallePrestamoResponse,
)
from src.crud.DetallePrestamo import (
    crear_detalle_prestamo,
    obtener_detalles,
    obtener_detalle_por_id,
    eliminar_detalle_prestamo,
)

router = APIRouter(prefix="/detalle-prestamo", tags=["DetallePrestamo"])


@router.post("/", response_model=DetallePrestamoResponse)
def crear(data: DetallePrestamoCreate, db: Session = Depends(get_db)):
    try:
        return crear_detalle_prestamo(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[DetallePrestamoResponse])
def listar(db: Session = Depends(get_db)):
    return obtener_detalles(db)


@router.get("/{id_detalle}", response_model=DetallePrestamoResponse)
def obtener(id_detalle: UUID, db: Session = Depends(get_db)):
    detalle = obtener_detalle_por_id(db, id_detalle)

    if not detalle:
        raise HTTPException(status_code=404, detail="Detalle no encontrado")

    return detalle


@router.delete("/{id_detalle}")
def eliminar(id_detalle: UUID, db: Session = Depends(get_db)):
    success = eliminar_detalle_prestamo(db, id_detalle)

    if not success:
        raise HTTPException(status_code=404, detail="Detalle no encontrado")

    return {"message": "Detalle eliminado"}
