from sqlalchemy.orm import Session
# Estructura corregida según las carpetas del proyecto general
from entities.Prestamo import Prestamo
from entities.Detalle_Prestamo import DetallePrestamo
from entities.multa import Multa

class PrestamoService:
    # CREAR UN PRESTAMO
    def crear_prestamo(self, db: Session, id_usuario, fecha_dev_prevista, id_creador):
        nuevo = Prestamo(
            id_usuario=id_usuario,
            fecha_devolucion_prevista=fecha_dev_prevista,
            id_usuario_creacion=id_creador
        )
        db.add(nuevo)
        db.commit()
        db.refresh(nuevo)
        return nuevo

    # LEER PRESTAMOS
    def obtener_prestamos(self, db: Session):
        return db.query(Prestamo).all()

    # AGREGAR LIBROS AL PRESTAMO
    def agregar_detalle(self, db: Session, id_prestamo, id_libro, cantidad):
        detalle = DetallePrestamo(id_prestamo=id_prestamo, id_libro=id_libro, cantidad=cantidad)
        db.add(detalle)
        db.commit()
        return detalle

    # GENERAR UNA MULTA
    def generar_multa(self, db: Session, id_prestamo, monto, motivo, id_creador):
        nueva_multa = Multa(
            id_prestamo=id_prestamo, 
            monto=monto, 
            motivo=motivo, 
            id_usuario_creacion=id_creador
        )
        db.add(nueva_multa)
        db.commit()
        return nueva_multa