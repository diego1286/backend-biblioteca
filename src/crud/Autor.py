from typing import List, Optional
from uuid import UUID

from src.database.config import SessionLocal
from src.entities.Autor import Autor

db = SessionLocal()


def crear_autor(
    nombre: str,
    apellido: str,
    nacionalidad: str,
    id_usuario_crea: UUID,
) -> Autor:

    autor = Autor(
        nombre=nombre.strip(),
        apellido=apellido.strip(),
        nacionalidad=nacionalidad.strip(),
        id_usuario_crea=id_usuario_crea,
    )

    db.add(autor)
    db.commit()
    db.refresh(autor)
    return autor


def obtener_autor_por_id(id_autor: UUID) -> Optional[Autor]:
    return db.query(Autor).filter(Autor.id_autor == id_autor).first()


def obtener_autores() -> List[Autor]:
    return db.query(Autor).all()


def actualizar_autor(
    id_autor: UUID,
    id_usuario_edita: UUID,
    **kwargs,
) -> Optional[Autor]:

    autor = obtener_autor_por_id(id_autor)
    if not autor:
        return None

    for key, value in kwargs.items():
        setattr(autor, key, value)

    autor.id_usuario_edita = id_usuario_edita

    db.commit()
    db.refresh(autor)
    return autor


def eliminar_autor(id_autor: UUID) -> bool:
    autor = obtener_autor_por_id(id_autor)
    if not autor:
        return False

    db.delete(autor)
    db.commit()
    return True
