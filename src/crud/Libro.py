from typing import List, Optional
from uuid import UUID

from src.database.config import SessionLocal
from src.entities.Libro import Libro

db = SessionLocal()


def crear_libro(
    titulo: str,
    isbn: str,
    anio_publicacion: int,
    id_editorial: int,
    id_categoria: int,
    id_usuario_crea: UUID,
) -> Libro:

    # Validar ISBN único
    existe = db.query(Libro).filter(Libro.isbn == isbn.strip()).first()
    if existe:
        raise ValueError("El ISBN ya está registrado")

    libro = Libro(
        titulo=titulo.strip(),
        isbn=isbn.strip(),
        anio_publicacion=anio_publicacion,
        id_editorial=id_editorial,
        id_categoria=id_categoria,
        id_usuario_crea=id_usuario_crea,
    )

    db.add(libro)
    db.commit()
    db.refresh(libro)
    return libro


def obtener_libro_por_id(id_libro: UUID) -> Optional[Libro]:
    return db.query(Libro).filter(Libro.id_libro == id_libro).first()


def obtener_libros() -> List[Libro]:
    return db.query(Libro).all()


def actualizar_libro(
    id_libro: UUID,
    id_usuario_edita: UUID,
    **kwargs,
) -> Optional[Libro]:

    libro = obtener_libro_por_id(id_libro)
    if not libro:
        return None

    # Validar ISBN si se quiere actualizar
    if "isbn" in kwargs:
        nuevo_isbn = kwargs["isbn"].strip()
        existe = (
            db.query(Libro)
            .filter(Libro.isbn == nuevo_isbn, Libro.id_libro != id_libro)
            .first()
        )
        if existe:
            raise ValueError("El ISBN ya está registrado por otro libro")
        kwargs["isbn"] = nuevo_isbn

    # Limpiar strings
    if "titulo" in kwargs:
        kwargs["titulo"] = kwargs["titulo"].strip()

    for key, value in kwargs.items():
        setattr(libro, key, value)

    libro.id_usuario_edita = id_usuario_edita

    db.commit()
    db.refresh(libro)
    return libro


def eliminar_libro(id_libro: UUID) -> bool:
    libro = obtener_libro_por_id(id_libro)
    if not libro:
        return False

    db.delete(libro)
    db.commit()
    return True
