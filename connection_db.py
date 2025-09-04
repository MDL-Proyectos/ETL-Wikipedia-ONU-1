import psycopg2
from dotenv import load_dotenv
import os


#validación de variables de entorno.
load_dotenv()
#print("Conectando a la base de datos...")
#print(f"Host: {os.getenv('DB_HOST')}")
#print(f"Database: {os.getenv('DB_DATABASE')}")
#print(f"Port: {os.getenv('DB_PORT')}")
#print(f"User: {os.getenv('DB_USER')}")

# Parámetros de conexión
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_DATABASE"),
    port=os.getenv("DB_PORT"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PSS")
)

cur = conn.cursor()

# Crea la tabla si no existe
cur.execute("""
    CREATE TABLE IF NOT EXISTS paises_onu (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100),
        denominacion VARCHAR(100),
        fecha_admision DATE,        
        notas VARCHAR(150)  
    );
""")
conn.commit()

cur.execute("SELECT version();")
print(cur.fetchone())

# Cerrar cursor y conexión
cur.close()
conn.close()