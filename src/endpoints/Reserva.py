from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.config import get_db
from src.schemas.Reserva import ReservaCreate, ReservaResponse, ReservaUpdate
from src.crud.Reserva import (
    crear_reserva,
    obtener_reservas,
    obtener_reserva,
    actualizar_reserva,
    eliminar_reserva,
)

router = APIRouter(prefix="/reservas", tags=["Reservas"])


@router.post("/", response_model=ReservaResponse)
def crear(reserva: ReservaCreate, db: Session = Depends(get_db)):
    return crear_reserva(db, reserva)


@router.get("/", response_model=list[ReservaResponse])
def listar(db: Session = Depends(get_db)):
    return obtener_reservas(db)


@router.get("/{id_reserva}", response_model=ReservaResponse)
def obtener(id_reserva: str, db: Session = Depends(get_db)):
    return obtener_reserva(db, id_reserva)


@router.put("/{id_reserva}", response_model=ReservaResponse)
def actualizar(id_reserva: str, datos: ReservaUpdate, db: Session = Depends(get_db)):
    return actualizar_reserva(db, id_reserva, datos)


@router.delete("/{id_reserva}")
def eliminar(id_reserva: str, db: Session = Depends(get_db)):
    return eliminar_reserva(db, id_reserva)
