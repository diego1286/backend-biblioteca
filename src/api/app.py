from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import src.entities.Autor
import src.entities.Categoria
import src.entities.Editorial
import src.entities.Ejemplar
import src.entities.Libro
import src.entities.Prestamo
import src.entities.Usuario
import src.entities.DetallePrestamo
import src.entities.LibroAutor
import src.entities.Empleado
import src.entities.Multa
import src.entities.Reserva

# importar endpoints
from src.endpoints import Autor
from src.endpoints import usuario
from src.endpoints import Libro
from src.endpoints import Ejemplar
from src.endpoints import Prestamo
from src.endpoints import DetallePrestamo
from src.endpoints import LibroAutor
from src.endpoints import Multa
from src.endpoints import Reserva
from src.endpoints import Editorial
from src.endpoints import Empleado
from src.endpoints import Categoria

app = FastAPI(title="Api Biblioteca", version="1.0.0")

# ---------------- CORS ----------------
origins = ["https://biblioteca-backend-de011.web.app", "http://localhost:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
app.include_router(Autor.router)
app.include_router(usuario.router)
app.include_router(Libro.router)
app.include_router(Ejemplar.router)
app.include_router(Prestamo.router)
app.include_router(DetallePrestamo.router)
app.include_router(LibroAutor.router)
app.include_router(Multa.router)
app.include_router(Reserva.router)
app.include_router(Editorial.router)
app.include_router(Empleado.router)
app.include_router(Categoria.router)


# ruta base del api
@app.get("/")
def root():
    return {"message": "Api Biblioteca "}
