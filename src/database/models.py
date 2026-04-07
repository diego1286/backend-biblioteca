"""
Importa los modelos que deben registrarse en SQLAlchemy.
"""

from src.entities.Autor import Autor
from src.entities.Categoria import Categoria
from src.entities.Editorial import Editorial
from src.entities.Ejemplar import Ejemplar
from src.entities.Empleado import Empleado
from src.entities.Libro import Libro
from src.entities.Prestamo import Prestamo
from src.entities.Reserva import Reserva
from src.entities.Usuario import Usuario

__all__ = [
    "Autor",
    "Categoria",
    "Editorial",
    "Ejemplar",
    "Empleado",
    "Libro",
    "Prestamo",
    "Reserva",
    "Usuario",
]
