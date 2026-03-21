"""
Operaciones CRUD para Empleado
"""

from typing import List, Optional
from uuid import UUID
from datetime import date

from src.database.config import SessionLocal
from src.entities.Empleado import Empleado
from src.entities.Usuario import Usuario

db = SessionLocal()


# =========================
# CREATE
# =========================
def crear_empleado(
    id_usuario: UUID,
    cargo: str,
    fecha_contratacion: date,
    tipo_contrato: str,
    id_usuario_creacion: UUID,
    salario: float = None,
    estado: str = "activo",
) -> Empleado:

    # 🔹 Validaciones
    if not cargo or len(cargo.strip()) == 0:
        raise ValueError("El cargo es obligatorio")

    if len(cargo) > 100:
        raise ValueError("El cargo no puede exceder 100 caracteres")

    if salario is not None and salario < 0:
        raise ValueError("El salario no puede ser negativo")

    if not tipo_contrato or len(tipo_contrato.strip()) == 0:
        raise ValueError("El tipo de contrato es obligatorio")

    if estado not in ["activo", "inactivo", "suspendido"]:
        raise ValueError("Estado inválido")

    # 🔹 Validar usuario
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    if not usuario:
        raise ValueError("El usuario no existe")

    # 🔹 Validar que no exista ya un empleado para ese usuario
    existe = db.query(Empleado).filter(Empleado.id_usuario == id_usuario).first()
    if existe:
        raise ValueError("Este usuario ya es un empleado")

    empleado = Empleado(
        id_usuario=id_usuario,
        cargo=cargo.strip(),
        salario=salario,
        fecha_contratacion=fecha_contratacion,
        tipo_contrato=tipo_contrato.strip(),
        estado=estado,
        id_usuario_creacion=id_usuario_creacion,
    )

    db.add(empleado)
    db.commit()
    db.refresh(empleado)
    return empleado


# =========================
# READ
# =========================
def obtener_empleado_por_id(empleado_id: UUID) -> Optional[Empleado]:
    return db.query(Empleado).filter(Empleado.id_empleado == empleado_id).first()


def obtener_empleados() -> List[Empleado]:
    return db.query(Empleado).all()


def obtener_empleado_por_usuario(usuario_id: UUID) -> Optional[Empleado]:
    return db.query(Empleado).filter(Empleado.id_usuario == usuario_id).first()


def obtener_empleados_por_estado(estado: str) -> List[Empleado]:
    return db.query(Empleado).filter(Empleado.estado == estado).all()


# =========================
# UPDATE
# =========================
def actualizar_empleado(
    empleado_id: UUID,
    id_usuario_edita: UUID,
    **kwargs,
) -> Optional[Empleado]:

    empleado = obtener_empleado_por_id(empleado_id)
    if not empleado:
        return None

    # 🔹 Validaciones
    if "cargo" in kwargs:
        cargo = kwargs["cargo"]
        if not cargo or len(cargo.strip()) == 0:
            raise ValueError("El cargo es obligatorio")
        if len(cargo) > 100:
            raise ValueError("Máximo 100 caracteres")
        kwargs["cargo"] = cargo.strip()

    if "salario" in kwargs:
        salario = kwargs["salario"]
        if salario is not None and salario < 0:
            raise ValueError("El salario no puede ser negativo")

    if "estado" in kwargs:
        if kwargs["estado"] not in ["activo", "inactivo", "suspendido"]:
            raise ValueError("Estado inválido")

    if "tipo_contrato" in kwargs:
        tipo = kwargs["tipo_contrato"]
        if not tipo or len(tipo.strip()) == 0:
            raise ValueError("Tipo de contrato obligatorio")
        kwargs["tipo_contrato"] = tipo.strip()

    if "id_usuario" in kwargs:
        usuario = (
            db.query(Usuario).filter(Usuario.id_usuario == kwargs["id_usuario"]).first()
        )
        if not usuario:
            raise ValueError("El usuario no existe")

    # 🔹 Auditoría
    empleado.id_usuario_edita = id_usuario_edita

    # 🔹 Actualizar
    for key, value in kwargs.items():
        if hasattr(empleado, key):
            setattr(empleado, key, value)

    db.commit()
    db.refresh(empleado)
    return empleado


# =========================
# DELETE
# =========================
def eliminar_empleado(empleado_id: UUID) -> bool:

    empleado = obtener_empleado_por_id(empleado_id)
    if not empleado:
        return False

    db.delete(empleado)
    db.commit()
    return True
