"""

Operaciones CRUD para Editorial

"""
 
from typing import List, Optional

from uuid import UUID
 
from src.database.config import SessionLocal

from src.entities.Editorial import Editorial
 
db = SessionLocal()
 
 
# =========================

# CREATE

# =========================

def crear_editorial(nombre: str, pais: str) -> Editorial:
 
    if not nombre or len(nombre.strip()) == 0:

        raise ValueError("El nombre es obligatorio")
 
    if len(nombre) > 150:

        raise ValueError("Máximo 150 caracteres")
 
    if not pais or len(pais.strip()) == 0:

        raise ValueError("El país es obligatorio")
 
    # Validar nombre único

    existe = (

        db.query(Editorial)

        .filter(Editorial.nombre == nombre.strip())

        .first()

    )

    if existe:

        raise ValueError("La editorial ya existe")
 
    editorial = Editorial(

        nombre=nombre.strip(),

        pais=pais.strip(),

    )
 
    db.add(editorial)

    db.commit()

    db.refresh(editorial)

    return editorial
 
 
# =========================

# READ

# =========================

def obtener_editorial_por_id(id_editorial: UUID) -> Optional[Editorial]:

    return db.query(Editorial).filter(Editorial.id_editorial == id_editorial).first()
 
 
def obtener_editoriales() -> List[Editorial]:

    return db.query(Editorial).all()
 
 
def buscar_editorial_por_nombre(nombre: str) -> List[Editorial]:

    return db.query(Editorial).filter(Editorial.nombre.contains(nombre)).all()
 
 
# =========================

# UPDATE

# =========================

def actualizar_editorial(

    id_editorial: UUID,

    **kwargs,

) -> Optional[Editorial]:
 
    editorial = obtener_editorial_por_id(id_editorial)

    if not editorial:

        return None
 
    if "nombre" in kwargs:

        nombre = kwargs["nombre"]
 
        if not nombre or len(nombre.strip()) == 0:

            raise ValueError("El nombre es obligatorio")
 
        if len(nombre) > 150:

            raise ValueError("Máximo 150 caracteres")
 
        # Validar duplicado

        existe = (

            db.query(Editorial)

            .filter(

                Editorial.nombre == nombre.strip(),

                Editorial.id_editorial != id_editorial,

            )

            .first()

        )

        if existe:

            raise ValueError("Ya existe otra editorial con ese nombre")
 
        kwargs["nombre"] = nombre.strip()
 
    if "pais" in kwargs:

        pais = kwargs["pais"]
 
        if not pais or len(pais.strip()) == 0:

            raise ValueError("El país es obligatorio")
 
        kwargs["pais"] = pais.strip()
 
    for key, value in kwargs.items():

        setattr(editorial, key, value)
 
    db.commit()

    db.refresh(editorial)

    return editorial
 
 
# =========================

# DELETE

# =========================

def eliminar_editorial(id_editorial: UUID) -> bool:
 
    editorial = obtener_editorial_por_id(id_editorial)

    if not editorial:

        return False
 
    db.delete(editorial)

    db.commit()

    return True
 