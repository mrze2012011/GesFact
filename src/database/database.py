import sqlite3
import os

class Database:
    def __init__(self, db_path="gesfact.db"):
        self.db_path = db_path
        self._crear_tabla_usuarios()

    def conectar(self):
        return sqlite3.connect(self.db_path)

    def _crear_tabla_usuarios(self):
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )
            """)
            conn.commit()

    def insertar_usuario(self, nombre, email, password):
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO usuarios (nombre, email, password) VALUES (?, ?, ?)",
                (nombre, email, password)
            )
            conn.commit()

    def obtener_usuario_por_email(self, email):
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, nombre, email, password FROM usuarios WHERE email = ?",
                (email,)
            )
            row = cursor.fetchone()
            if row:
                return {"id": row[0], "nombre": row[1], "email": row[2], "password": row[3]}
            return None

# Instancia global
db = Database()
