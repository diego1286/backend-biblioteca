"""
Operaciones CRUD para Empleado
"""

from typing import List, Optional
from uuid import UUID
from datetime import date

from sqlalchemy.orm import Session

from src.entities.Empleado import Empleado


class EmpleadoCRUD:
    def __init__(self, db: Session):
        self.db = db

    # =========================
    # CREATE
    # =========================
    def crear_empleado(
        self,
        id_usuario: UUID,
        cargo: str,
        fecha_contratacion: date,
        tipo_contrato: str,
        id_usuario_creacion: UUID,
        salario: float = None,
        estado: str = "activo",
    ) -> Empleado:
        """
        Crear un empleado con validaciones
        """

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

        # 🔹 Validar usuario existente
        from entities.Usuario import Usuario

        usuario = (
            self.db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        )
        if not usuario:
            raise ValueError("El usuario no existe")

        # 🔹 Crear empleado
        empleado = Empleado(
            id_usuario=id_usuario,
            cargo=cargo.strip(),
            salario=salario,
            fecha_contratacion=fecha_contratacion,
            tipo_contrato=tipo_contrato.strip(),
            estado=estado,
            id_usuario_creacion=id_usuario_creacion,
        )

        self.db.add(empleado)
        self.db.commit()
        self.db.refresh(empleado)

        return empleado

    # =========================
    # READ
    # =========================
    def obtener_empleado(self, empleado_id: UUID) -> Optional[Empleado]:
        """
        Obtener un empleado por ID
        """
        return (
            self.db.query(Empleado).filter(Empleado.id_empleado == empleado_id).first()
        )

    def obtener_empleados(self, skip: int = 0, limit: int = 100) -> List[Empleado]:
        """
        Obtener lista de empleados
        """
        return self.db.query(Empleado).offset(skip).limit(limit).all()

    def obtener_empleado_por_usuario(self, usuario_id: UUID) -> Optional[Empleado]:
        """
        Obtener empleado por ID de usuario
        """
        return self.db.query(Empleado).filter(Empleado.id_usuario == usuario_id).first()

    def obtener_empleados_por_estado(self, estado: str) -> List[Empleado]:
        """
        Obtener empleados por estado
        """
        return self.db.query(Empleado).filter(Empleado.estado == estado).all()

    # =========================
    # UPDATE
    # =========================
    def actualizar_empleado(
        self, empleado_id: UUID, id_usuario_edita: UUID, **kwargs
    ) -> Optional[Empleado]:
        """
        Actualizar empleado con validaciones
        """

        empleado = self.obtener_empleado(empleado_id)
        if not empleado:
            return None

        # 🔹 Validaciones dinámicas
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
            from entities.Usuario import Usuario

            usuario = (
                self.db.query(Usuario)
                .filter(Usuario.id_usuario == kwargs["id_usuario"])
                .first()
            )
            if not usuario:
                raise ValueError("El usuario no existe")

        # 🔹 Auditoría
        empleado.id_usuario_edita = id_usuario_edita

        # 🔹 Actualizar campos
        for key, value in kwargs.items():
            if hasattr(empleado, key):
                setattr(empleado, key, value)

        self.db.commit()
        self.db.refresh(empleado)

        return empleado

    # =========================
    # DELETE
    # =========================
    def eliminar_empleado(self, empleado_id: UUID) -> bool:
        """
        Eliminar empleado
        """
        empleado = self.obtener_empleado(empleado_id)

        if empleado:
            self.db.delete(empleado)
            self.db.commit()
            return True

        return False
