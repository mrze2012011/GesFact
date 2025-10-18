import sqlite3
import os

class Database:
    def __init__(self):
        # Configurar path de la base de datos
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.db_path = os.path.join(base_dir, "database", "gesfact.db")
        
        # Asegurar que la carpeta database existe
        database_dir = os.path.dirname(self.db_path)
        if not os.path.exists(database_dir):
            os.makedirs(database_dir)
        
        # SOLO crear conexión, NO crear tablas aquí
        # Las tablas serán creadas por auth_service
        print("✅ Conexión a base de datos configurada")
    
    def get_connection(self):
        """Obtener conexión a la base de datos"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Para acceso por nombre de columna
        return conn

# Instancia global para que otros módulos la usen
db = Database()