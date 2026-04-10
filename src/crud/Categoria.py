from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session

from src.entities.Categoria import Categoria
from src.schemas.Categoria import CategoriaCreate, CategoriaUpdate


def crear_categoria(db: Session, data: CategoriaCreate) -> Categoria:

    existe = db.query(Categoria).filter(Categoria.nombre == data.nombre.strip()).first()

    if existe:
        raise ValueError("La categoría ya existe")

    categoria = Categoria(**data.model_dump())

    db.add(categoria)
    db.commit()
    db.refresh(categoria)

    return categoria


def obtener_categoria_por_id(db: Session, id_categoria: UUID) -> Optional[Categoria]:
    return db.query(Categoria).filter(Categoria.id_categoria == id_categoria).first()


def obtener_categorias(db: Session) -> List[Categoria]:
    return db.query(Categoria).all()


def actualizar_categoria(
    db: Session, id_categoria: UUID, data: CategoriaUpdate
) -> Optional[Categoria]:

    categoria = obtener_categoria_por_id(db, id_categoria)

    if not categoria:
        return None

    update_data = data.model_dump(exclude_unset=True)

    if "nombre" in update_data:
        nuevo_nombre = update_data["nombre"].strip().title()

        existe = (
            db.query(Categoria)
            .filter(
                Categoria.nombre == nuevo_nombre,
                Categoria.id_categoria != id_categoria,
            )
            .first()
        )

        if existe:
            raise ValueError("La categoría ya existe")

        update_data["nombre"] = nuevo_nombre

    for key, value in update_data.items():
        if isinstance(value, str):
            value = value.strip()

        setattr(categoria, key, value)

    db.commit()
    db.refresh(categoria)

    return categoria


def eliminar_categoria(db: Session, id_categoria: UUID) -> bool:

    categoria = obtener_categoria_por_id(db, id_categoria)

    if not categoria:
        return False

    db.delete(categoria)
    db.commit()

    return True
