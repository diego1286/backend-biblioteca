from typing import List, Optional
from uuid import UUID

from src.database.config import SessionLocal
from src.entities.Reserva import Reserva
from src.entities.Usuario import Usuario
from src.entities.Libro import Libro

db = SessionLocal()


# =========================
# CREATE
# =========================
def crear_reserva(
    id_usuario: UUID,
    id_libro: UUID,
    id_usuario_creacion: UUID,
    estado: str = "activa",
) -> Reserva:

    if estado not in ["activa", "cancelada", "completada"]:
        raise ValueError("Estado inválido")

    # Validar usuario
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    if not usuario:
        raise ValueError("El usuario no existe")

    # Validar libro
    libro = db.query(Libro).filter(Libro.id_libro == id_libro).first()
    if not libro:
        raise ValueError("El libro no existe")

    # Validar reserva duplicada
    existe = (
        db.query(Reserva)
        .filter(
            Reserva.id_usuario == id_usuario,
            Reserva.id_libro == id_libro,
            Reserva.estado == "activa",
        )
        .first()
    )
    if existe:
        raise ValueError("Ya existe una reserva activa para este libro")

    reserva = Reserva(
        id_usuario=id_usuario,
        id_libro=id_libro,
        estado=estado,
        id_usuario_creacion=id_usuario_creacion,
    )

    db.add(reserva)
    db.commit()
    db.refresh(reserva)
    return reserva


# =========================
# READ
# =========================
def obtener_reserva_por_id(reserva_id: UUID) -> Optional[Reserva]:
    return db.query(Reserva).filter(Reserva.id_reserva == reserva_id).first()


def obtener_reservas() -> List[Reserva]:
    return db.query(Reserva).all()


def obtener_reservas_por_usuario(usuario_id: UUID) -> List[Reserva]:
    return db.query(Reserva).filter(Reserva.id_usuario == usuario_id).all()


def obtener_reservas_por_libro(libro_id: UUID) -> List[Reserva]:
    return db.query(Reserva).filter(Reserva.id_libro == libro_id).all()


def obtener_reservas_por_estado(estado: str) -> List[Reserva]:
    return db.query(Reserva).filter(Reserva.estado == estado).all()


# =========================
# UPDATE
# =========================
def actualizar_reserva(
    reserva_id: UUID,
    id_usuario_edita: UUID,
    **kwargs,
) -> Optional[Reserva]:

    reserva = obtener_reserva_por_id(reserva_id)
    if not reserva:
        return None

    # Validar estado
    if "estado" in kwargs:
        if kwargs["estado"] not in ["activa", "cancelada", "completada"]:
            raise ValueError("Estado inválido")

    # Validar usuario
    if "id_usuario" in kwargs:
        usuario = (
            db.query(Usuario).filter(Usuario.id_usuario == kwargs["id_usuario"]).first()
        )
        if not usuario:
            raise ValueError("El usuario no existe")

    # Validar libro
    if "id_libro" in kwargs:
        libro = db.query(Libro).filter(Libro.id_libro == kwargs["id_libro"]).first()
        if not libro:
            raise ValueError("El libro no existe")

    # Actualizar campos
    for key, value in kwargs.items():
        if hasattr(reserva, key):
            setattr(reserva, key, value)

    reserva.id_usuario_edita = id_usuario_edita

    db.commit()
    db.refresh(reserva)
    return reserva


# =========================
# DELETE
# =========================
def eliminar_reserva(reserva_id: UUID) -> bool:
    reserva = obtener_reserva_por_id(reserva_id)

    if not reserva:
        return False

    db.delete(reserva)
    db.commit()
    return True
