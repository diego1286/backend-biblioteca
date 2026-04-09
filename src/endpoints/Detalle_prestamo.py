from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.config import get_db
from src.schemas.Detalle_prestamo import DetallePrestamoCreate, DetallePrestamoResponse
from src.crud.Detalle_prestamo import crear_detalle, obtener_detalles

router = APIRouter(prefix="/detalles-prestamos", tags=["Detalles de Préstamos"])

@router.post("/", response_model=DetallePrestamoResponse)
def create_detalle_endpoint(detalle: DetallePrestamoCreate, db: Session = Depends(get_db)):
    return crear_detalle(db, detalle)

@router.get("/", response_model=list[DetallePrestamoResponse])
def get_detalles_endpoint(db: Session = Depends(get_db)):
    return obtener_detalles(db)