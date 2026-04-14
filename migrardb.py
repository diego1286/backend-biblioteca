"""
Script para crear las tablas en Neon (PostgreSQL).
Ejecutar una vez después de configurar DATABASE_URL en .env:

python init_db.py

No es necesario levantar la API; este script solo aplica el esquema.
"""

import os

from dotenv import load_dotenv
from sqlalchemy.exc import OperationalError

import src.entities.Autor
import src.entities.Categoria
import src.entities.DetallePrestamo
import src.entities.Editorial
import src.entities.Ejemplar
import src.entities.Empleado
import src.entities.Libro
import src.entities.LibroAutor
import src.entities.Prestamo
import src.entities.Usuario
import src.entities.Multa
import src.entities.Reserva
from src.database.config import create_tables


load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))


try:
    create_tables()
    print("Se crearon las tablas en Neon")
except OperationalError as e:
    if "password authentication failed" in str(e).lower():
        print("Conexion rechazada por password")
        print("revisa la conexion al neon ttps://console.neon.tech")
        print("Copia la conexion String (Connection String) u¿y actualiza .env")
    else:
        print("Error de conexion a la base de datos:", e)
    raise SystemExit(1)
