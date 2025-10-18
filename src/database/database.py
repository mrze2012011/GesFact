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
        
        self._create_tables()
    
    def get_connection(self):
        """Obtener conexión a la base de datos"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Para acceso por nombre de columna
        return conn
    
    def _create_tables(self):
        """Crear tablas si no existen"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # SOLO tabla de usuarios (tu compañero agregará las demás)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_completo TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                nombre_negocio TEXT NOT NULL,
                fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
        
        print("✅ Base de datos inicializada correctamente")

# Instancia global para que otros módulos la usen
db = Database()