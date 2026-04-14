from pydantic import BaseModel
from uuid import UUID
from datetime import date, datetime
from decimal import Decimal


class EmpleadoBase(BaseModel):
    cargo: str
    salario: Decimal | None = None
    fecha_contratacion: date
    tipo_contrato: str
    estado: str = "activo"


class EmpleadoCreate(EmpleadoBase):
    id_usuario: UUID
    id_usuario_creacion: UUID


class EmpleadoUpdate(BaseModel):
    cargo: str | None = None
    salario: Decimal | None = None
    tipo_contrato: str | None = None
    estado: str | None = None
    id_usuario_edita: UUID | None = None


class EmpleadoResponse(EmpleadoBase):
    id_empleado: UUID
    id_usuario: UUID
    fecha_creacion: datetime

    class Config:
        from_attributes = True
