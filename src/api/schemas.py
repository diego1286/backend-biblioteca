from datetime import date, datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ORMModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class AutorBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    apellido: str = Field(..., min_length=1, max_length=100)
    nacionalidad: str = Field(..., min_length=1, max_length=100)
    id_usuario_crea: Optional[UUID] = None


class AutorCreate(AutorBase):
    pass


class AutorUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    apellido: Optional[str] = Field(None, min_length=1, max_length=100)
    nacionalidad: Optional[str] = Field(None, min_length=1, max_length=100)
    id_usuario_edita: Optional[UUID] = None


class AutorRead(ORMModel):
    id_autor: UUID
    nombre: str
    apellido: str
    nacionalidad: str
    id_usuario_crea: Optional[UUID]
    id_usuario_edita: Optional[UUID]
    fecha_creacion: Optional[datetime]
    fecha_edicion: Optional[datetime]


class CategoriaBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    descripcion: Optional[str] = None


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    descripcion: Optional[str] = None


class CategoriaRead(ORMModel):
    id_categoria: UUID
    nombre: str
    descripcion: Optional[str]


class EditorialBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=150)
    pais: str = Field(..., min_length=1, max_length=100)


class EditorialCreate(EditorialBase):
    pass


class EditorialUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=1, max_length=150)
    pais: Optional[str] = Field(None, min_length=1, max_length=100)


class EditorialRead(ORMModel):
    id_editorial: UUID
    nombre: str
    pais: str


class UsuarioBase(BaseModel):
    nombre_usuario: str = Field(..., min_length=1, max_length=150)
    rol: str = Field(..., min_length=1, max_length=50)
    contrasena: str = Field(..., min_length=1, max_length=255)
    activo: bool = True


class UsuarioCreate(UsuarioBase):
    pass


class UsuarioUpdate(BaseModel):
    nombre_usuario: Optional[str] = Field(None, min_length=1, max_length=150)
    rol: Optional[str] = Field(None, min_length=1, max_length=50)
    contrasena: Optional[str] = Field(None, min_length=1, max_length=255)
    activo: Optional[bool] = None


class UsuarioRead(ORMModel):
    id_usuario: UUID
    nombre_usuario: str
    rol: str
    activo: bool
    fecha_creacion: Optional[datetime]
    fecha_edicion: Optional[datetime]


class LibroBase(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=255)
    isbn: str = Field(..., min_length=1, max_length=50)
    anio_publicacion: int
    id_editorial: UUID
    id_categoria: UUID
    id_usuario_crea: Optional[UUID] = None


class LibroCreate(LibroBase):
    pass


class LibroUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=1, max_length=255)
    isbn: Optional[str] = Field(None, min_length=1, max_length=50)
    anio_publicacion: Optional[int] = None
    id_editorial: Optional[UUID] = None
    id_categoria: Optional[UUID] = None
    id_usuario_edita: Optional[UUID] = None


class LibroRead(ORMModel):
    id_libro: UUID
    titulo: str
    isbn: str
    anio_publicacion: int
    id_editorial: UUID
    id_categoria: UUID
    id_usuario_crea: Optional[UUID]
    id_usuario_edita: Optional[UUID]
    fecha_creacion: Optional[datetime]
    fecha_edicion: Optional[datetime]


class EjemplarBase(BaseModel):
    id_libro: UUID
    codigo_barra: str = Field(..., min_length=1, max_length=100)
    estado: str = Field(..., min_length=1, max_length=50)
    ubicacion: str = Field(..., min_length=1, max_length=100)
    id_usuario_crea: Optional[UUID] = None


class EjemplarCreate(EjemplarBase):
    pass


class EjemplarUpdate(BaseModel):
    id_libro: Optional[UUID] = None
    codigo_barra: Optional[str] = Field(None, min_length=1, max_length=100)
    estado: Optional[str] = Field(None, min_length=1, max_length=50)
    ubicacion: Optional[str] = Field(None, min_length=1, max_length=100)
    id_usuario_edita: Optional[UUID] = None


class EjemplarRead(ORMModel):
    id_ejemplar: UUID
    id_libro: UUID
    codigo_barra: str
    estado: str
    ubicacion: str
    id_usuario_crea: Optional[UUID]
    id_usuario_edita: Optional[UUID]
    fecha_creacion: Optional[datetime]
    fecha_edicion: Optional[datetime]


class EmpleadoBase(BaseModel):
    id_usuario: UUID
    cargo: str = Field(..., min_length=1, max_length=100)
    salario: Optional[Decimal] = None
    fecha_contratacion: date
    tipo_contrato: str = Field(..., min_length=1, max_length=50)
    estado: str = Field(default="activo")
    id_usuario_creacion: UUID


class EmpleadoCreate(EmpleadoBase):
    pass


class EmpleadoUpdate(BaseModel):
    id_usuario: Optional[UUID] = None
    cargo: Optional[str] = Field(None, min_length=1, max_length=100)
    salario: Optional[Decimal] = None
    fecha_contratacion: Optional[date] = None
    tipo_contrato: Optional[str] = Field(None, min_length=1, max_length=50)
    estado: Optional[str] = None
    id_usuario_edita: Optional[UUID] = None


class EmpleadoRead(ORMModel):
    id_empleado: UUID
    id_usuario: UUID
    cargo: str
    salario: Optional[Decimal]
    fecha_contratacion: date
    tipo_contrato: str
    estado: str
    id_usuario_creacion: UUID
    id_usuario_edita: Optional[UUID]
    fecha_creacion: Optional[datetime]
    fecha_edicion: Optional[datetime]


class PrestamoBase(BaseModel):
    id_usuario: UUID
    id_empleado: UUID
    fecha_prestamo: date
    fecha_devolucion_estimada: date
    fecha_devolucion_real: Optional[date] = None
    estado: str = Field(..., min_length=1, max_length=50)
    id_usuario_crea: Optional[UUID] = None


class PrestamoCreate(PrestamoBase):
    pass


class PrestamoUpdate(BaseModel):
    id_usuario: Optional[UUID] = None
    id_empleado: Optional[UUID] = None
    fecha_prestamo: Optional[date] = None
    fecha_devolucion_estimada: Optional[date] = None
    fecha_devolucion_real: Optional[date] = None
    estado: Optional[str] = Field(None, min_length=1, max_length=50)
    id_usuario_edita: Optional[UUID] = None


class PrestamoRead(ORMModel):
    id_prestamo: UUID
    id_usuario: UUID
    id_empleado: UUID
    fecha_prestamo: date
    fecha_devolucion_estimada: date
    fecha_devolucion_real: Optional[date]
    estado: str
    id_usuario_crea: Optional[UUID]
    id_usuario_edita: Optional[UUID]
    fecha_creacion: Optional[datetime]
    fecha_edicion: Optional[datetime]


class ReservaBase(BaseModel):
    id_usuario: UUID
    id_libro: UUID
    estado: str = Field(default="activa", min_length=1, max_length=20)
    id_usuario_creacion: UUID


class ReservaCreate(ReservaBase):
    pass


class ReservaUpdate(BaseModel):
    id_usuario: Optional[UUID] = None
    id_libro: Optional[UUID] = None
    estado: Optional[str] = Field(None, min_length=1, max_length=20)
    id_usuario_edita: Optional[UUID] = None


class ReservaRead(ORMModel):
    id_reserva: UUID
    id_usuario: UUID
    id_libro: UUID
    estado: str
    id_usuario_creacion: UUID
    id_usuario_edita: Optional[UUID]
    fecha_creacion: Optional[datetime]
    fecha_edicion: Optional[datetime]
