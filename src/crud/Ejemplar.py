from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import HTTPException

from src.entities.Ejemplar import Ejemplar
from src.schemas.Ejemplar import EjemplarCreate, EjemplarUpdate


# Crear ejemplar
def crear_Ejemplar(db: Session, data: EjemplarCreate) -> Ejemplar:
    existe = (
        db.query(Ejemplar).filter(Ejemplar.codigo_barra == data.codigo_barra).first()
    )

    if existe:
        raise HTTPException(status_code=400, detail="El codigo de barra ya existe")

    ejemplar = Ejemplar(**data.model_dump())

    db.add(ejemplar)
    db.commit()
    db.refresh(ejemplar)

    return ejemplar


# obtener ejemplar por id
def obtener_ejemplar_por_id(db: Session, id_ejemplar: UUID) -> Optional[Ejemplar]:
    return db.query(Ejemplar).filter(Ejemplar.id_ejemplar == id_ejemplar).first()


# Listar ejemplares
def obtener_ejemplares(db: Session) -> List[Ejemplar]:
    return db.query(Ejemplar).all()


# Actualizar ejemplar
def actualizar_ejemplar(
    db: Session, id_ejemplar: UUID, data: EjemplarUpdate
) -> Optional[Ejemplar]:

    ejemplar = obtener_ejemplar_por_id(db, id_ejemplar)
    if not ejemplar:
        return None

    update_data = data.model_dump(exclude_unset=True)

    if "codigo_barra" in update_data:
        nuevo_codigo = update_data["codigo_barra"].strip()

        existe = (
            db.query(Ejemplar)
            .filter(
                Ejemplar.codigo_barra == nuevo_codigo,
                Ejemplar.id_ejemplar != id_ejemplar,
            )
            .first()
        )

        if existe:
            raise ValueError("El codigo de barra ya está registrado")

        update_data["codigo_barra"] = nuevo_codigo

    for key, value in update_data.items():
        if isinstance(value, str):
            value = value.strip()

        setattr(ejemplar, key, value)

    db.commit()
    db.refresh(ejemplar)

    return ejemplar


def eliminar_ejemplar(db: Session, id_ejemplar: UUID) -> bool:
    ejemplar = obtener_ejemplar_por_id(db, id_ejemplar)
    if not ejemplar:
        return False

    db.delete(ejemplar)
    db.commit()
    return True
