from sqlalchemy.orm import Session
from uuid import UUID

from src.entities.LibroAutor import LibroAutor


def asignar_autor_a_libro(db: Session, id_libro: UUID, id_autor: UUID):

    # Validar si ya existe
    existe = (
        db.query(LibroAutor)
        .filter(LibroAutor.id_libro == id_libro, LibroAutor.id_autor == id_autor)
        .first()
    )

    if existe:
        return existe

    relacion = LibroAutor(id_libro=id_libro, id_autor=id_autor)

    db.add(relacion)
    db.commit()
    return relacion


def eliminar_autor_de_libro(db: Session, id_libro: UUID, id_autor: UUID):

    relacion = (
        db.query(LibroAutor)
        .filter(LibroAutor.id_libro == id_libro, LibroAutor.id_autor == id_autor)
        .first()
    )

    if not relacion:
        return False

    db.delete(relacion)
    db.commit()
    return True
