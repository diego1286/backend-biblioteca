import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

# SQL directo: Esto no falla por culpa de otros
sql_tablas = """
CREATE TABLE IF NOT EXISTS tbl_prestamos (
    id_prestamo SERIAL PRIMARY KEY,
    id_usuario INTEGER,
    fecha_prestamo TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS tbl_detalles_prestamos (
    id_detalle SERIAL PRIMARY KEY,
    id_prestamo INTEGER,
    id_libro INTEGER,
    cantidad INTEGER
);

CREATE TABLE IF NOT EXISTS tbl_multas (
    id_multa SERIAL PRIMARY KEY,
    id_usuario_creacion INTEGER,
    monto DECIMAL(10,2),
    motivo TEXT
);
"""

if __name__ == "__main__":
    try:
        print("🚀 Intentando conexión forzada a Neon...")
        with engine.connect() as conn:
            conn.execute(text(sql_tablas))
            conn.commit()
            print("✅ ¡LAS TABLAS SE CREARON EN LA NUBE!")
            
            # Verificación
            res = conn.execute(text("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname = 'public'"))
            print(f"📋 Tablas actuales: {[r[0] for r in res]}")
    except Exception as e:
        print(f"❌ Error de conexión: {e}")