from sqlalchemy.orm import Session
from src.entities.Empleado import Empleado


def crear_empleado(db: Session, data):
    empleado = Empleado(**data.dict())
    db.add(empleado)
    db.commit()
    db.refresh(empleado)
    return empleado


def obtener_empleados(db: Session):
    return db.query(Empleado).all()


def obtener_empleado(db: Session, id_empleado):
    return db.query(Empleado).filter(Empleado.id_empleado == id_empleado).first()


def actualizar_empleado(db: Session, id_empleado, data):
    empleado = obtener_empleado(db, id_empleado)

    if not empleado:
        return None

    for key, value in data.dict(exclude_unset=True).items():
        setattr(empleado, key, value)

    db.commit()
    db.refresh(empleado)
    return empleado


def eliminar_empleado(db: Session, id_empleado):
    empleado = obtener_empleado(db, id_empleado)

    if not empleado:
        return None

    db.delete(empleado)
    db.commit()
    return empleado
