"""
Operaciones CRUD para Categoria
"""
from typing import List, Optional
from uuid import UUID
from src.database.config import SessionLocal
from src.entities.Categoria import Categoria
db = SessionLocal()

# =========================
# CREATE
# =========================
def crear_categoria(nombre: str, descripcion: str = None) -> Categoria:
    if not nombre or len(nombre.strip()) == 0:
        raise ValueError("El nombre es obligatorio")
    if len(nombre) > 100:
        raise ValueError("Máximo 100 caracteres")
    # Validar nombre único
    existe = (
        db.query(Categoria)
        .filter(Categoria.nombre == nombre.strip())
        .first()
    )
    if existe:
        raise ValueError("La categoría ya existe")
    categoria = Categoria(
        nombre=nombre.strip(),
        descripcion=descripcion.strip() if descripcion else None,
    )
    db.add(categoria)
    db.commit()
    db.refresh(categoria)
    return categoria

# =========================
# READ
# =========================
def obtener_categoria_por_id(id_categoria: UUID) -> Optional[Categoria]:
    return db.query(Categoria).filter(Categoria.id_categoria == id_categoria).first()

def obtener_categorias() -> List[Categoria]:
    return db.query(Categoria).all()

def buscar_categoria_por_nombre(nombre: str) -> List[Categoria]:
    return db.query(Categoria).filter(Categoria.nombre.contains(nombre)).all()

# =========================
# UPDATE
# =========================
def actualizar_categoria(
    id_categoria: UUID,
    **kwargs,
) -> Optional[Categoria]:
    categoria = obtener_categoria_por_id(id_categoria)
    if not categoria:
        return None
    if "nombre" in kwargs:
        nombre = kwargs["nombre"]
        if not nombre or len(nombre.strip()) == 0:
            raise ValueError("El nombre es obligatorio")
        if len(nombre) > 100:
            raise ValueError("Máximo 100 caracteres")
        # Validar duplicado
        existe = (
            db.query(Categoria)
            .filter(
                Categoria.nombre == nombre.strip(),
                Categoria.id_categoria != id_categoria,
            )
            .first()
        )
        if existe:
            raise ValueError("Ya existe otra categoría con ese nombre")
        kwargs["nombre"] = nombre.strip()
    if "descripcion" in kwargs and kwargs["descripcion"]:
        kwargs["descripcion"] = kwargs["descripcion"].strip()
    for key, value in kwargs.items():
        setattr(categoria, key, value)
    db.commit()
    db.refresh(categoria)
    return categoria

# =========================
# DELETE
# =========================
def eliminar_categoria(id_categoria: UUID) -> bool:
    categoria = obtener_categoria_por_id(id_categoria)
    if not categoria:
        return False
    db.delete(categoria)
    db.commit()
    return True