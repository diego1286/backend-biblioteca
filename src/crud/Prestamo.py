from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session

from src.entities.Prestamo import Prestamo


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

    for key, value in data.model_dump(exclude_unset=True).items():
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
