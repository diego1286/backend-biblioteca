from fastapi import FastAPI
import src.entities

# importar endpoints
from src.endpoints import Autor
from src.endpoints import usuario
from src.endpoints import Libro
from src.endpoints import Ejemplar
from src.endpoints import Prestamo
from src.endpoints import DetallePrestamo
from src.endpoints import LibroAutor

app = FastAPI(title="Api Biblioteca", version="1.0.0")

# Rutas
app.include_router(Autor.router)
app.include_router(usuario.router)
app.include_router(Libro.router)
app.include_router(Ejemplar.router)
app.include_router(Prestamo.router)
app.include_router(DetallePrestamo.router)
app.include_router(LibroAutor.router)


# ruta base del api
@app.get("/")
def root():
    return {"message": "Api Biblioteca "}
