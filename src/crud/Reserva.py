from sqlalchemy.orm import Session
from src.entities.Reserva import Reserva
from src.schemas.Reserva import ReservaCreate, ReservaUpdate


def crear_reserva(db: Session, reserva: ReservaCreate):
    nueva = Reserva(**reserva.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


def obtener_reservas(db: Session):
    return db.query(Reserva).all()


def obtener_reserva(db: Session, id_reserva):
    return db.query(Reserva).filter(Reserva.id_reserva == id_reserva).first()


def actualizar_reserva(db: Session, id_reserva, datos: ReservaUpdate):
    reserva = obtener_reserva(db, id_reserva)
    if reserva:
        for key, value in datos.dict(exclude_unset=True).items():
            setattr(reserva, key, value)
        db.commit()
        db.refresh(reserva)
    return reserva


def eliminar_reserva(db: Session, id_reserva):
    reserva = obtener_reserva(db, id_reserva)
    if reserva:
        db.delete(reserva)
        db.commit()
    return reserva
