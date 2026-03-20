from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Cargar variables del .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

try:
    # Crear conexión
    engine = create_engine(DATABASE_URL)

    # Probar conexión
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("✅ Conexión exitosa a la base de datos")

except Exception as e:
    print(" Error de conexión:")
    print(e)
