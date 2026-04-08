from fastapi import FastAPI

# importar endpoints
from src.endpoints import Autor
from src.endpoints import Usuario
from src.endpoints import Libro
from src.endpoints import Ejemplar
from src.endpoints import Prestamo


app = FastAPI(title="Api Biblioteca", version="1.0.0")

# Rutas
app.include_router(Autor.router)
app.include_router(Usuario.router)
app.include_router(Libro.router)
app.include_router(Ejemplar.router)
app.include_router(Prestamo.router)


# ruta base del api
@app.get("/")
def root():
    return {"message": "Api Biblioteca "}
