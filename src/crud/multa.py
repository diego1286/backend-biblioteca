from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from src.entities.multa import Multa
from src.schemas.multa import MultaCreate, MultaUpdate

def crear_multa(db: Session, data: MultaCreate) -> Multa:
    multa = Multa(**data.model_dump())
    db.add(multa)
    db.commit()
    db.refresh(multa)
    return multa

def obtener_multa_por_id(db: Session, id_multa: UUID) -> Optional[Multa]:
    return db.query(Multa).filter(Multa.id_multa == id_multa).first()

def obtener_multas(db: Session) -> List[Multa]:
    return db.query(Multa).all()

def actualizar_multa(db: Session, id_multa: UUID, data: MultaUpdate) -> Optional[Multa]:
    multa = obtener_multa_por_id(db, id_multa)
    if not multa:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(multa, key, value)
    db.commit()
    db.refresh(multa)
    return multa

def eliminar_multa(db: Session, id_multa: UUID) -> bool:
    multa = obtener_multa_por_id(db, id_multa)
    if not multa:
        return False
    db.delete(multa)
    db.commit()
    return True