import psycopg2
from dotenv import load_dotenv
import os

class PostgresDB:
    def __init__(self):
        load_dotenv()
        self.conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_DATABASE"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PSS")
        )
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS paises_onu (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(100),
                denominacion VARCHAR(100),
                fecha_admision DATE,
                notas VARCHAR(250)
            );
        """)
        self.conn.commit()

    def load_to_db(self, datos):
        registros = 0
        for dato in datos:
            self.cur.execute("""
                INSERT INTO paises_onu (nombre, denominacion, fecha_admision, notas)
                VALUES (%s, %s, %s, %s)
            """, (
                dato.get("Estado miembro"),
                dato.get("Denominación UNTERM"),
                dato.get("Fecha de admisión"),
                dato.get("Notas")
            ))
            registros += 1
        self.conn.commit()
        return registros

    def close(self):
        self.cur.close()
        self.conn.close()