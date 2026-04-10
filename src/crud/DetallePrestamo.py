from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session

from src.entities.DetallePrestamo import DetallePrestamo
from src.entities.Ejemplar import Ejemplar


def crear_detalle_prestamo(db: Session, data) -> DetallePrestamo:

    # VALIDACIÓN
    ejemplar = (
        db.query(Ejemplar).filter(Ejemplar.id_ejemplar == data.id_ejemplar).first()
    )

    if not ejemplar:
        raise ValueError("El ejemplar no existe")

    # Validar que no esté prestado
    if ejemplar.estado.lower() == "prestado":
        raise ValueError("El ejemplar ya está prestado")

    detalle = DetallePrestamo(**data.model_dump())

    # Cambiar estado del ejemplar
    ejemplar.estado = "prestado"

    db.add(detalle)
    db.commit()
    db.refresh(detalle)

    return detalle


def obtener_detalles(db: Session) -> List[DetallePrestamo]:
    return db.query(DetallePrestamo).all()


def obtener_detalle_por_id(db: Session, id_detalle: UUID) -> Optional[DetallePrestamo]:
    return (
        db.query(DetallePrestamo)
        .filter(DetallePrestamo.id_detalle == id_detalle)
        .first()
    )


def eliminar_detalle_prestamo(db: Session, id_detalle: UUID) -> bool:

    detalle = obtener_detalle_por_id(db, id_detalle)

    if not detalle:
        return False

    # 🔥 devolver ejemplar
    ejemplar = (
        db.query(Ejemplar).filter(Ejemplar.id_ejemplar == detalle.id_ejemplar).first()
    )

    if ejemplar:
        ejemplar.estado = "disponible"

    db.delete(detalle)
    db.commit()

    return True
