from typing import List, Optional
from uuid import UUID

from src.database.config import SessionLocal
from src.entities.Prestamo import Prestamo

db = SessionLocal()


def crear_prestamo(
    id_usuario: UUID,
    id_empleado: UUID,
    fecha_prestamo: Date,
    fecha_devolucion_estimada: Date,
    fecha_devolucion_real: Date,
    estado: str,
    id_usuario_crea: UUID,
) -> Prestamo:
    # validacion de fechas
    if fecha_devolucion_estimada < fecha_prestamo:
        raise ValueError("La fecha de devolucion no puede ser menor")

    prestamo = Prestamo(
        id_usuario=id_usuario,
        id_empleado=id_empleado,
        fecha_prestamo=fecha_prestamo,
        fecha_devolucion_estimada=fecha_devolucion_estimada,
        estado=estado.strip(),
        id_usuario_crea=id_usuario_crea,
    )

    db.add(prestamo)
    db.commit()
    db.refresh(prestamo)
    return prestamo


# obtener un  prestamo por Id
def obtener_prestamo_por_id(id_prestamo: UUID) -> Optional[Prestamo]:
    return db.query(Prestamo).filter(Prestamo.id_prestamo == id_prestamo).first()


# obtener la lista de prestamos que hay
def obter_lista_prestamos() -> List[Prestamo]:
    return db.query(Prestamo).all()


# actualizar el listado de prestamo
def actualizar_presstamos(
    id_prestamo: UUID,
    id_usuario_edita: UUID,
    **kwargs,
) -> Optional[Prestamo]:
    prestamo = obtener_prestamo_por_id(id_prestamo)
    if not prestamo:
        return None

    # validacion de fechas para actualizar
    fecha_prestamo = kwargs.get("fecha_prestamo", prestamo.fecha_prestamo)
    fecha_dev_est = kwargs.get(
        "fecha_devolucion_estimada", prestamo.fecha_devolucion_estimada
    )
    if fecha_dev_est < fecha_prestamo:
        raise ValueError("La fecha de devolucion no puede ser menor")

    # limpiar estado
    if "estado" in kwargs:
        kwargs["estado"] = kwargs["estado"].strip()

    for key, value in kwargs.items():
        setattr(prestamo, key, value)

    prestamo.id_usuario_edita = id_usuario_edita

    db.commit()
    db.refresh(prestamo)
    return prestamo


# eliminar prestamo
def eliminar_prestamo(id_prestamo: UUID) -> bool:
    prestamo = obtener_prestamo_por_id(id_prestamo)
    if not prestamo:
        return False
    db.delete(prestamo)
    db.commit()
    return True
