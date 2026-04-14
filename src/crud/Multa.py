from sqlalchemy.orm import Session
from src.entities.Multa import Multa
from src.schemas.Multa import MultaCreate, MultaUpdate


def crear_multa(db: Session, multa: MultaCreate):
    nueva = Multa(**multa.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


def obtener_multas(db: Session):
    return db.query(Multa).all()


def obtener_multa(db: Session, id_multa):
    return db.query(Multa).filter(Multa.id_multa == id_multa).first()


def actualizar_multa(db: Session, id_multa, datos: MultaUpdate):
    multa = obtener_multa(db, id_multa)
    if multa:
        for key, value in datos.dict(exclude_unset=True).items():
            setattr(multa, key, value)
        db.commit()
        db.refresh(multa)
    return multa


def eliminar_multa(db: Session, id_multa):
    multa = obtener_multa(db, id_multa)
    if multa:
        db.delete(multa)
        db.commit()
    return multa
