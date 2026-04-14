from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.config import get_db

from src.schemas.Empleado import (
    EmpleadoCreate,
    EmpleadoResponse,
    EmpleadoUpdate,
)
from src.crud.Empleado import (
    crear_empleado,
    obtener_empleados,
    obtener_empleado,
    actualizar_empleado,
    eliminar_empleado,
)

router = APIRouter(prefix="/empleados", tags=["Empleados"])


@router.post("/", response_model=EmpleadoResponse)
def crear(data: EmpleadoCreate, db: Session = Depends(get_db)):
    return crear_empleado(db, data)


@router.get("/", response_model=list[EmpleadoResponse])
def listar(db: Session = Depends(get_db)):
    return obtener_empleados(db)


@router.get("/{id_empleado}", response_model=EmpleadoResponse)
def obtener(id_empleado: str, db: Session = Depends(get_db)):
    empleado = obtener_empleado(db, id_empleado)
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado


@router.put("/{id_empleado}", response_model=EmpleadoResponse)
def actualizar(id_empleado: str, data: EmpleadoUpdate, db: Session = Depends(get_db)):
    empleado = actualizar_empleado(db, id_empleado, data)
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado


@router.delete("/{id_empleado}")
def eliminar(id_empleado: str, db: Session = Depends(get_db)):
    empleado = eliminar_empleado(db, id_empleado)
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return {"message": "Empleado eliminado"}
