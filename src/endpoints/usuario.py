from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from src.database.config import get_db
from src.schemas.Usuario import UsuarioCreate, UsuarioUpdate, UsuarioResponse
from src.crud.Usuario import *

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.post("/", response_model=UsuarioResponse)
def crearUsuario(data: UsuarioCreate, db: Session = Depends(get_db)):
    return crear_usuario(db, data)


@router.get("/", response_model=list[UsuarioResponse])
def listarUsuario(db: Session = Depends(get_db)):
    return obtener_usuarios(db)


@router.get("/{id_usuario}", response_model=UsuarioResponse)
def UsuarioXID(id_usuario: UUID, db: Session = Depends(get_db)):
    usuario = obtener_usuario_por_id(db, id_usuario)

    if not usuario:
        raise HTTPException(404, " Usuario no encontrado")
    return usuario


@router.put("/{id_usuario}", response_model=UsuarioResponse)
def actualizarUsuario(
    id_usuario: UUID, data: UsuarioUpdate, db: Session = Depends(get_db)
):
    usuario = actualizar_usuario(db, id_usuario, data)

    if not usuario:
        raise HTTPException(404, "Usuario no encontrado")
    return usuario


@router.delete("/{id_usuario}")
def eliminar(id_usuario: UUID, db: Session = Depends(get_db)):
    success = eliminar_usuario(db, id_usuario)

    if not success:
        raise HTTPException(404, "Usuario no encontrado")

    return {"message": "Usuario eliminado"}
