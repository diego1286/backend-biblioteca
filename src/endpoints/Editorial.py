from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.config import get_db
from src.schemas.Editorial import (
    EditorialCreate,
    EditorialResponse,
    EditorialUpdate,
)
from src.crud.Editorial import (
    crear_editorial,
    obtener_editoriales,
    obtener_editorial,
    actualizar_editorial,
    eliminar_editorial,
)

router = APIRouter(prefix="/editoriales", tags=["Editoriales"])


@router.post("/", response_model=EditorialResponse)
def crear(editorial: EditorialCreate, db: Session = Depends(get_db)):
    return crear_editorial(db, editorial)


@router.get("/", response_model=list[EditorialResponse])
def listar(db: Session = Depends(get_db)):
    return obtener_editoriales(db)


@router.get("/{id_editorial}", response_model=EditorialResponse)
def obtener(id_editorial: str, db: Session = Depends(get_db)):
    return obtener_editorial(db, id_editorial)


@router.put("/{id_editorial}", response_model=EditorialResponse)
def actualizar(
    id_editorial: str, datos: EditorialUpdate, db: Session = Depends(get_db)
):
    return actualizar_editorial(db, id_editorial, datos)


@router.delete("/{id_editorial}")
def eliminar(id_editorial: str, db: Session = Depends(get_db)):
    return eliminar_editorial(db, id_editorial)
