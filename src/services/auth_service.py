import sqlite3
import hashlib
import os
from datetime import datetime

class AuthService:
    def __init__(self, db_path):
        self.db_path = db_path
        self._crear_tabla_usuarios()
    
    def _crear_tabla_usuarios(self):
        """Crea la tabla de usuarios si no existe"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_completo TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                nombre_negocio TEXT NOT NULL,
                fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def _hash_password(self, password):
        """Genera el hash de la contraseña"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def registrar_usuario(self, nombre_completo, email, password, nombre_negocio):
        """Registra un nuevo usuario en la base de datos"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Verificar si el email ya existe
            cursor.execute("SELECT id FROM usuarios WHERE email = ?", (email,))
            if cursor.fetchone():
                return False, "El email ya está registrado"
            
            # Hashear contraseña
            password_hash = self._hash_password(password)
            
            # Insertar nuevo usuario
            cursor.execute('''
                INSERT INTO usuarios (nombre_completo, email, password_hash, nombre_negocio)
                VALUES (?, ?, ?, ?)
            ''', (nombre_completo, email, password_hash, nombre_negocio))
            
            conn.commit()
            conn.close()
            return True, "Usuario registrado exitosamente"
            
        except sqlite3.Error as e:
            return False, f"Error de base de datos: {str(e)}"
    
    def login_usuario(self, email, password):
        """Valida las credenciales del usuario"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Buscar usuario por email
            cursor.execute('''
                SELECT id, nombre_completo, password_hash, nombre_negocio 
                FROM usuarios WHERE email = ?
            ''', (email,))
            
            usuario = cursor.fetchone()
            conn.close()
            
            if not usuario:
                return False, "Usuario no encontrado"
            
            # Verificar contraseña
            password_hash = self._hash_password(password)
            if usuario[2] == password_hash:
                usuario_data = {
                    'id': usuario[0],
                    'nombre_completo': usuario[1],
                    'email': email,
                    'nombre_negocio': usuario[3],
                    'logueado': True
                }
                return True, usuario_data
            else:
                return False, "Contraseña incorrecta"
                
        except sqlite3.Error as e:
            return False, f"Error de base de datos: {str(e)}"
    
    def verificar_email_existente(self, email):
        """Verifica si un email ya está registrado"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute("SELECT id FROM usuarios WHERE email = ?", (email,))
            existe = cursor.fetchone() is not None
            
            conn.close()
            return existe
            
        except sqlite3.Error:
            return False

# Instancia global del servicio de autenticación
# Se inicializará desde main.py con la ruta de la base de datos
auth_service = None

def inicializar_auth_service(db_path):
    """Inicializa el servicio de autenticación con la ruta de la base de datos"""
    global auth_service
    auth_service = AuthService(db_path)