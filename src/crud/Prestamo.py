from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session

from src.entities.Prestamo import Prestamo
from src.schemas.Prestamo import PrestamoCreate, PrestamoUpdate


def crear_prestamo(db: Session, data: PrestamoCreate) -> Prestamo:

    if data.fecha_devolucion_estimada < data.fecha_prestamo:
        raise ValueError("Fecha estimada inválida")

    prestamo = Prestamo(**data.model_dump())

    db.add(prestamo)
    db.commit()
    db.refresh(prestamo)
    return prestamo


def obtener_prestamo_por_id(db: Session, id_prestamo: UUID) -> Optional[Prestamo]:
    return db.query(Prestamo).filter(Prestamo.id_prestamo == id_prestamo).first()


def obtener_prestamos(db: Session) -> List[Prestamo]:
    return db.query(Prestamo).all()


def actualizar_prestamo(
    db: Session, id_prestamo: UUID, data: PrestamoUpdate
) -> Optional[Prestamo]:

    prestamo = obtener_prestamo_por_id(db, id_prestamo)

    if not prestamo:
        return None

    update_data = data.model_dump(exclude_unset=True)

    # Validaciones
    if "fecha_devolucion_real" in update_data:
        if update_data["fecha_devolucion_real"] < prestamo.fecha_prestamo:
            raise ValueError("Fecha de devolución inválida")

    if "estado" in update_data and isinstance(update_data["estado"], str):
        update_data["estado"] = update_data["estado"].strip().lower()

    for key, value in update_data.items():
        setattr(prestamo, key, value)

    db.commit()
    db.refresh(prestamo)
    return prestamo


def eliminar_prestamo(db: Session, id_prestamo: UUID) -> bool:
    prestamo = obtener_prestamo_por_id(db, id_prestamo)

    if not prestamo:
        return False

    db.delete(prestamo)
    db.commit()
    return True
