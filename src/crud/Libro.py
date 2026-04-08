from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session


from src.entities.Libro import Libro
from src.schemas.Libro import createLibro, updateLibro


# crearLibro
def crear_libro(db: Session, data: createLibro) -> Libro:

    # Validar ISBN único
    existe = db.query(Libro).filter(Libro.isbn == data.isbn).first()
    if existe:
        raise ValueError("El ISBN ya está registrado")

    libro = Libro(**data.model_dump())

    db.add(libro)
    db.commit()
    db.refresh(libro)
    return libro


def obtener_libro_por_id(db: Session, id_libro: UUID) -> Optional[Libro]:
    return db.query(Libro).filter(Libro.id_libro == id_libro).first()


def obtener_libros(db: Session) -> List[Libro]:
    return db.query(Libro).all()


def actualizar_libro(db: Session, id_libro: UUID, data: updateLibro) -> Optional[Libro]:

    libro = obtener_libro_por_id(db, id_libro)
    if not libro:
        return None

    update_data = data.model_dump(exclude_unset=True)

    # Validar ISBN si se quiere actualizar
    if "isbn" in update_data:
        existe = (
            db.query(Libro)
            .filter(Libro.isbn == update_data["isbn"], Libro.id_libro != id_libro)
            .first()
        )
        if existe:
            raise ValueError("El ISBN ya está registrado por otro libro")
        kwargs["isbn"] = nuevo_isbn

    for key, value in update_data.items():
        if isinstance(value, str):
            value = value.strip()
        setattr(libro, key, value)

    db.commit()
    db.refresh(libro)
    return libro


def eliminar_libro(db: Session, id_libro: UUID) -> bool:
    libro = obtener_libro_por_id(DB, id_libro)
    if not libro:
        return False

    db.delete(libro)
    db.commit()
    return True
