from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session

from src.entities.Usuario import Usuario
from src.schemas.Usuario import UsuarioCreate, UsuarioUpdate


# crear usuario
def crear_usuario(db: Session, data: UsuarioCreate) -> Usuario:

    usuario = Usuario(**data.model_dump())

    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario


# obtener por ID
def obtener_usuario_por_id(db: Session, id_usuario: UUID) -> Optional[Usuario]:
    return db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()


# obtener usuarios
def obtener_usuarios(db: Session) -> List[Usuario]:
    return db.query(Usuario).all()


# Actualizar Usuario
def actualizar_usuario(
    db: Session, id_usuario: UUID, data: UsuarioUpdate
) -> Optional[Usuario]:

    usuario = obtener_usuario_por_id(db, id_usuario)
    if not usuario:
        return None

    for key, value in data.model_dump(exclude_unset=True).items():
        if isinstance(value, str):
            value = value.strip()
        setattr(usuario, key, value)

    db.commit()
    db.refresh(usuario)
    return usuario


# Eliminar Usuario
def eliminar_usuario(db: Session, id_usuario: UUID) -> bool:
    usuario = obtener_usuario_por_id(db, id_usuario)
    if not usuario:
        return False

    db.delete(usuario)
    db.commit()
    return True
