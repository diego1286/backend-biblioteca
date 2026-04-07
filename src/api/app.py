from fastapi import FastAPI

# importar endpoints
from src.endpoints import Autor

app = FastAPI(title="Api Biblioteca", version="1.0.0")

# Rutas
app.include_router(Autor.router)

# ruta base del api


@app.get("/")
def root():
    return {"message": "Api Biblioteca "}
