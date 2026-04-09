from sqlalchemy.orm import Session
# Asegúrate de que aquí también diga Detalle_prestamo (con p minúscula)
from src.entities.Detalle_prestamo import DetallePrestamo 
from src.schemas.Detalle_prestamo import DetallePrestamoCreate

def crear_detalle(db: Session, detalle: DetallePrestamoCreate):
    db_detalle = DetallePrestamo(
        id_prestamo=detalle.id_prestamo,
        id_libro=detalle.id_libro,
        cantidad=detalle.cantidad
    )
    db.add(db_detalle)
    db.commit()
    db.refresh(db_detalle)
    return db_detalle

def obtener_detalles(db: Session):
    return db.query(DetallePrestamo).all()