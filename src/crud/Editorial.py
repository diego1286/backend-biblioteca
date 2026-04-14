from sqlalchemy.orm import Session
from src.entities.Editorial import Editorial
from src.schemas.Editorial import EditorialCreate, EditorialUpdate


def crear_editorial(db: Session, editorial: EditorialCreate):
    nueva = Editorial(**editorial.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


def obtener_editoriales(db: Session):
    return db.query(Editorial).all()


def obtener_editorial(db: Session, id_editorial):
    return db.query(Editorial).filter(Editorial.id_editorial == id_editorial).first()


def actualizar_editorial(db: Session, id_editorial, datos: EditorialUpdate):
    editorial = obtener_editorial(db, id_editorial)
    if editorial:
        for key, value in datos.dict(exclude_unset=True).items():
            setattr(editorial, key, value)
        db.commit()
        db.refresh(editorial)
    return editorial


def eliminar_editorial(db: Session, id_editorial):
    editorial = obtener_editorial(db, id_editorial)
    if editorial:
        db.delete(editorial)
        db.commit()
    return editorial
