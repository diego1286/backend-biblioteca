from typing import List, Optional
from uuid import UUID

from src.database.config import SessionLocal
from src.entities.Usuario import Usuario

db = SessionLocal()


def crear_usuario(
    nombre_usuario: str,
    rol: str,
    contrasena: str,
    activo: bool = True,
) -> Usuario:

    usuario = Usuario(
        nombre_usuario=nombre_usuario.strip(),
        rol=rol.strip(),
        contrasena=contrasena.strip(),
        activo=activo,
    )

    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario


def obtener_usuario_por_id(id_usuario: UUID) -> Optional[Usuario]:
    return db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()


def obtener_usuarios() -> List[Usuario]:
    return db.query(Usuario).all()


def actualizar_usuario(
    id_usuario: UUID,
    **kwargs,
) -> Optional[Usuario]:

    usuario = obtener_usuario_por_id(id_usuario)
    if not usuario:
        return None

    # Limpiar strings
    if "nombre_usuario" in kwargs:
        kwargs["nombre_usuario"] = kwargs["nombre_usuario"].strip()

    if "rol" in kwargs:
        kwargs["rol"] = kwargs["rol"].strip()

    if "contrasena" in kwargs:
        kwargs["contrasena"] = kwargs["contrasena"].strip()

    for key, value in kwargs.items():
        setattr(usuario, key, value)

    db.commit()
    db.refresh(usuario)
    return usuario


def eliminar_usuario(id_usuario: UUID) -> bool:
    usuario = obtener_usuario_por_id(id_usuario)
    if not usuario:
        return False

    db.delete(usuario)
    db.commit()
    return True
