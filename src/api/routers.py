from typing import Any
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.api import schemas
from src.database.config import get_db
from src.entities.Autor import Autor
from src.entities.Categoria import Categoria
from src.entities.Editorial import Editorial
from src.entities.Ejemplar import Ejemplar
from src.entities.Empleado import Empleado
from src.entities.Libro import Libro
from src.entities.Prestamo import Prestamo
from src.entities.Reserva import Reserva
from src.entities.Usuario import Usuario

api_router = APIRouter()


def commit_instance(db: Session, instance: Any):
    try:
        db.add(instance)
        db.commit()
        db.refresh(instance)
        return instance
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No fue posible completar la operacion por restricciones de integridad.",
        ) from exc


def get_or_404(db: Session, model: type, entity_id: UUID, field_name: str):
    instance = db.query(model).filter(getattr(model, field_name) == entity_id).first()
    if not instance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{model.__name__} no encontrado",
        )
    return instance


@api_router.get("/autores", response_model=list[schemas.AutorRead], tags=["Autores"])
def listar_autores(db: Session = Depends(get_db)):
    return db.query(Autor).all()


@api_router.get("/autores/{autor_id}", response_model=schemas.AutorRead, tags=["Autores"])
def obtener_autor(autor_id: UUID, db: Session = Depends(get_db)):
    return get_or_404(db, Autor, autor_id, "id_autor")


@api_router.post(
    "/autores",
    response_model=schemas.AutorRead,
    status_code=status.HTTP_201_CREATED,
    tags=["Autores"],
)
def crear_autor(payload: schemas.AutorCreate, db: Session = Depends(get_db)):
    autor = Autor(**payload.model_dump())
    return commit_instance(db, autor)


@api_router.put("/autores/{autor_id}", response_model=schemas.AutorRead, tags=["Autores"])
def actualizar_autor(
    autor_id: UUID,
    payload: schemas.AutorUpdate,
    db: Session = Depends(get_db),
):
    autor = get_or_404(db, Autor, autor_id, "id_autor")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(autor, key, value)
    return commit_instance(db, autor)


@api_router.delete(
    "/autores/{autor_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Autores"],
)
def eliminar_autor(autor_id: UUID, db: Session = Depends(get_db)):
    autor = get_or_404(db, Autor, autor_id, "id_autor")
    db.delete(autor)
    db.commit()


@api_router.get("/categorias", response_model=list[schemas.CategoriaRead], tags=["Categorias"])
def listar_categorias(db: Session = Depends(get_db)):
    return db.query(Categoria).all()


@api_router.get(
    "/categorias/{categoria_id}",
    response_model=schemas.CategoriaRead,
    tags=["Categorias"],
)
def obtener_categoria(categoria_id: UUID, db: Session = Depends(get_db)):
    return get_or_404(db, Categoria, categoria_id, "id_categoria")


@api_router.post(
    "/categorias",
    response_model=schemas.CategoriaRead,
    status_code=status.HTTP_201_CREATED,
    tags=["Categorias"],
)
def crear_categoria(payload: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    categoria = Categoria(**payload.model_dump())
    return commit_instance(db, categoria)


@api_router.put(
    "/categorias/{categoria_id}",
    response_model=schemas.CategoriaRead,
    tags=["Categorias"],
)
def actualizar_categoria(
    categoria_id: UUID,
    payload: schemas.CategoriaUpdate,
    db: Session = Depends(get_db),
):
    categoria = get_or_404(db, Categoria, categoria_id, "id_categoria")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(categoria, key, value)
    return commit_instance(db, categoria)


@api_router.delete(
    "/categorias/{categoria_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Categorias"],
)
def eliminar_categoria(categoria_id: UUID, db: Session = Depends(get_db)):
    categoria = get_or_404(db, Categoria, categoria_id, "id_categoria")
    db.delete(categoria)
    db.commit()


@api_router.get("/editoriales", response_model=list[schemas.EditorialRead], tags=["Editoriales"])
def listar_editoriales(db: Session = Depends(get_db)):
    return db.query(Editorial).all()


@api_router.get(
    "/editoriales/{editorial_id}",
    response_model=schemas.EditorialRead,
    tags=["Editoriales"],
)
def obtener_editorial(editorial_id: UUID, db: Session = Depends(get_db)):
    return get_or_404(db, Editorial, editorial_id, "id_editorial")


@api_router.post(
    "/editoriales",
    response_model=schemas.EditorialRead,
    status_code=status.HTTP_201_CREATED,
    tags=["Editoriales"],
)
def crear_editorial(payload: schemas.EditorialCreate, db: Session = Depends(get_db)):
    editorial = Editorial(**payload.model_dump())
    return commit_instance(db, editorial)


@api_router.put(
    "/editoriales/{editorial_id}",
    response_model=schemas.EditorialRead,
    tags=["Editoriales"],
)
def actualizar_editorial(
    editorial_id: UUID,
    payload: schemas.EditorialUpdate,
    db: Session = Depends(get_db),
):
    editorial = get_or_404(db, Editorial, editorial_id, "id_editorial")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(editorial, key, value)
    return commit_instance(db, editorial)


@api_router.delete(
    "/editoriales/{editorial_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Editoriales"],
)
def eliminar_editorial(editorial_id: UUID, db: Session = Depends(get_db)):
    editorial = get_or_404(db, Editorial, editorial_id, "id_editorial")
    db.delete(editorial)
    db.commit()


@api_router.get("/usuarios", response_model=list[schemas.UsuarioRead], tags=["Usuarios"])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()


@api_router.get("/usuarios/{usuario_id}", response_model=schemas.UsuarioRead, tags=["Usuarios"])
def obtener_usuario(usuario_id: UUID, db: Session = Depends(get_db)):
    return get_or_404(db, Usuario, usuario_id, "id_usuario")


@api_router.post(
    "/usuarios",
    response_model=schemas.UsuarioRead,
    status_code=status.HTTP_201_CREATED,
    tags=["Usuarios"],
)
def crear_usuario(payload: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    usuario = Usuario(**payload.model_dump())
    return commit_instance(db, usuario)


@api_router.put(
    "/usuarios/{usuario_id}",
    response_model=schemas.UsuarioRead,
    tags=["Usuarios"],
)
def actualizar_usuario(
    usuario_id: UUID,
    payload: schemas.UsuarioUpdate,
    db: Session = Depends(get_db),
):
    usuario = get_or_404(db, Usuario, usuario_id, "id_usuario")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(usuario, key, value)
    return commit_instance(db, usuario)


@api_router.delete(
    "/usuarios/{usuario_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Usuarios"],
)
def eliminar_usuario(usuario_id: UUID, db: Session = Depends(get_db)):
    usuario = get_or_404(db, Usuario, usuario_id, "id_usuario")
    db.delete(usuario)
    db.commit()


@api_router.get("/libros", response_model=list[schemas.LibroRead], tags=["Libros"])
def listar_libros(db: Session = Depends(get_db)):
    return db.query(Libro).all()


@api_router.get("/libros/{libro_id}", response_model=schemas.LibroRead, tags=["Libros"])
def obtener_libro(libro_id: UUID, db: Session = Depends(get_db)):
    return get_or_404(db, Libro, libro_id, "id_libro")


@api_router.post(
    "/libros",
    response_model=schemas.LibroRead,
    status_code=status.HTTP_201_CREATED,
    tags=["Libros"],
)
def crear_libro(payload: schemas.LibroCreate, db: Session = Depends(get_db)):
    libro = Libro(**payload.model_dump())
    return commit_instance(db, libro)


@api_router.put("/libros/{libro_id}", response_model=schemas.LibroRead, tags=["Libros"])
def actualizar_libro(
    libro_id: UUID,
    payload: schemas.LibroUpdate,
    db: Session = Depends(get_db),
):
    libro = get_or_404(db, Libro, libro_id, "id_libro")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(libro, key, value)
    return commit_instance(db, libro)


@api_router.delete(
    "/libros/{libro_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Libros"],
)
def eliminar_libro(libro_id: UUID, db: Session = Depends(get_db)):
    libro = get_or_404(db, Libro, libro_id, "id_libro")
    db.delete(libro)
    db.commit()


@api_router.get("/ejemplares", response_model=list[schemas.EjemplarRead], tags=["Ejemplares"])
def listar_ejemplares(db: Session = Depends(get_db)):
    return db.query(Ejemplar).all()


@api_router.get(
    "/ejemplares/{ejemplar_id}",
    response_model=schemas.EjemplarRead,
    tags=["Ejemplares"],
)
def obtener_ejemplar(ejemplar_id: UUID, db: Session = Depends(get_db)):
    return get_or_404(db, Ejemplar, ejemplar_id, "id_ejemplar")


@api_router.post(
    "/ejemplares",
    response_model=schemas.EjemplarRead,
    status_code=status.HTTP_201_CREATED,
    tags=["Ejemplares"],
)
def crear_ejemplar(payload: schemas.EjemplarCreate, db: Session = Depends(get_db)):
    ejemplar = Ejemplar(**payload.model_dump())
    return commit_instance(db, ejemplar)


@api_router.put(
    "/ejemplares/{ejemplar_id}",
    response_model=schemas.EjemplarRead,
    tags=["Ejemplares"],
)
def actualizar_ejemplar(
    ejemplar_id: UUID,
    payload: schemas.EjemplarUpdate,
    db: Session = Depends(get_db),
):
    ejemplar = get_or_404(db, Ejemplar, ejemplar_id, "id_ejemplar")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(ejemplar, key, value)
    return commit_instance(db, ejemplar)


@api_router.delete(
    "/ejemplares/{ejemplar_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Ejemplares"],
)
def eliminar_ejemplar(ejemplar_id: UUID, db: Session = Depends(get_db)):
    ejemplar = get_or_404(db, Ejemplar, ejemplar_id, "id_ejemplar")
    db.delete(ejemplar)
    db.commit()


@api_router.get("/empleados", response_model=list[schemas.EmpleadoRead], tags=["Empleados"])
def listar_empleados(db: Session = Depends(get_db)):
    return db.query(Empleado).all()


@api_router.get(
    "/empleados/{empleado_id}",
    response_model=schemas.EmpleadoRead,
    tags=["Empleados"],
)
def obtener_empleado(empleado_id: UUID, db: Session = Depends(get_db)):
    return get_or_404(db, Empleado, empleado_id, "id_empleado")


@api_router.post(
    "/empleados",
    response_model=schemas.EmpleadoRead,
    status_code=status.HTTP_201_CREATED,
    tags=["Empleados"],
)
def crear_empleado(payload: schemas.EmpleadoCreate, db: Session = Depends(get_db)):
    empleado = Empleado(**payload.model_dump())
    return commit_instance(db, empleado)


@api_router.put(
    "/empleados/{empleado_id}",
    response_model=schemas.EmpleadoRead,
    tags=["Empleados"],
)
def actualizar_empleado(
    empleado_id: UUID,
    payload: schemas.EmpleadoUpdate,
    db: Session = Depends(get_db),
):
    empleado = get_or_404(db, Empleado, empleado_id, "id_empleado")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(empleado, key, value)
    return commit_instance(db, empleado)


@api_router.delete(
    "/empleados/{empleado_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Empleados"],
)
def eliminar_empleado(empleado_id: UUID, db: Session = Depends(get_db)):
    empleado = get_or_404(db, Empleado, empleado_id, "id_empleado")
    db.delete(empleado)
    db.commit()


@api_router.get("/prestamos", response_model=list[schemas.PrestamoRead], tags=["Prestamos"])
def listar_prestamos(db: Session = Depends(get_db)):
    return db.query(Prestamo).all()


@api_router.get(
    "/prestamos/{prestamo_id}",
    response_model=schemas.PrestamoRead,
    tags=["Prestamos"],
)
def obtener_prestamo(prestamo_id: UUID, db: Session = Depends(get_db)):
    return get_or_404(db, Prestamo, prestamo_id, "id_prestamo")


@api_router.post(
    "/prestamos",
    response_model=schemas.PrestamoRead,
    status_code=status.HTTP_201_CREATED,
    tags=["Prestamos"],
)
def crear_prestamo(payload: schemas.PrestamoCreate, db: Session = Depends(get_db)):
    if payload.fecha_devolucion_estimada < payload.fecha_prestamo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La fecha de devolucion estimada no puede ser menor a la fecha del prestamo.",
        )
    prestamo = Prestamo(**payload.model_dump())
    return commit_instance(db, prestamo)


@api_router.put(
    "/prestamos/{prestamo_id}",
    response_model=schemas.PrestamoRead,
    tags=["Prestamos"],
)
def actualizar_prestamo(
    prestamo_id: UUID,
    payload: schemas.PrestamoUpdate,
    db: Session = Depends(get_db),
):
    prestamo = get_or_404(db, Prestamo, prestamo_id, "id_prestamo")
    data = payload.model_dump(exclude_unset=True)
    fecha_prestamo = data.get("fecha_prestamo", prestamo.fecha_prestamo)
    fecha_devolucion_estimada = data.get(
        "fecha_devolucion_estimada", prestamo.fecha_devolucion_estimada
    )
    if fecha_devolucion_estimada < fecha_prestamo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La fecha de devolucion estimada no puede ser menor a la fecha del prestamo.",
        )
    for key, value in data.items():
        setattr(prestamo, key, value)
    return commit_instance(db, prestamo)


@api_router.delete(
    "/prestamos/{prestamo_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Prestamos"],
)
def eliminar_prestamo(prestamo_id: UUID, db: Session = Depends(get_db)):
    prestamo = get_or_404(db, Prestamo, prestamo_id, "id_prestamo")
    db.delete(prestamo)
    db.commit()


@api_router.get("/reservas", response_model=list[schemas.ReservaRead], tags=["Reservas"])
def listar_reservas(db: Session = Depends(get_db)):
    return db.query(Reserva).all()


@api_router.get("/reservas/{reserva_id}", response_model=schemas.ReservaRead, tags=["Reservas"])
def obtener_reserva(reserva_id: UUID, db: Session = Depends(get_db)):
    return get_or_404(db, Reserva, reserva_id, "id_reserva")


@api_router.post(
    "/reservas",
    response_model=schemas.ReservaRead,
    status_code=status.HTTP_201_CREATED,
    tags=["Reservas"],
)
def crear_reserva(payload: schemas.ReservaCreate, db: Session = Depends(get_db)):
    reserva = Reserva(**payload.model_dump())
    return commit_instance(db, reserva)


@api_router.put(
    "/reservas/{reserva_id}",
    response_model=schemas.ReservaRead,
    tags=["Reservas"],
)
def actualizar_reserva(
    reserva_id: UUID,
    payload: schemas.ReservaUpdate,
    db: Session = Depends(get_db),
):
    reserva = get_or_404(db, Reserva, reserva_id, "id_reserva")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(reserva, key, value)
    return commit_instance(db, reserva)


@api_router.delete(
    "/reservas/{reserva_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Reservas"],
)
def eliminar_reserva(reserva_id: UUID, db: Session = Depends(get_db)):
    reserva = get_or_404(db, Reserva, reserva_id, "id_reserva")
    db.delete(reserva)
    db.commit()
