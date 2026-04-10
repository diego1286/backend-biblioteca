from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session

from src.entities.Autor import Autor
from src.schemas.Autor import AutorCreate, AutorUpdate


def crear_autor(db: Session, autor_data: AutorCreate) -> Autor:
    autor = Autor(**autor_data.model_dump())

    db.add(autor)
    db.commit()
    db.refresh(autor)
    return autor


def obtener_autor_por_id(db: Session, id_autor: UUID) -> Optional[Autor]:
    return db.query(Autor).filter(Autor.id_autor == id_autor).first()


def obtener_autores(db: Session) -> List[Autor]:
    return db.query(Autor).all()


def actualizar_autor(db: Session, id_autor: UUID, data: AutorUpdate) -> Optional[Autor]:
    autor = obtener_autor_por_id(db, id_autor)

    if not autor:
        return None

    for key, value in data.model_dump(exclude_unset=True).items():
        if isinstance(value, str):
            value = value.strip().title()

        setattr(autor, key, value)

    db.commit()
    db.refresh(autor)
    return autor


def eliminar_autor(db: Session, id_autor: UUID) -> bool:
    autor = obtener_autor_por_id(db, id_autor)

    if not autor:
        return False

    db.delete(autor)
    db.commit()
    return True
