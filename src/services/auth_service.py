import hashlib
from src.database.database import db

class AuthService:
    def __init__(self):
        self._crear_tabla_usuarios()
    
    def _crear_tabla_usuarios(self):
        """Crea la tabla de usuarios si no existe"""
        conn = db.get_connection()
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
    
    def _validar_email(self, email):
        """Valida formato básico de email"""
        return '@' in email and '.' in email and len(email) > 5
    
    def _validar_password(self, password):
        """Valida fortaleza de contraseña"""
        return len(password) >= 6
    
    def registrar_usuario(self, nombre_completo, email, password, confirm_password, nombre_negocio):
        """Registra un nuevo usuario con validaciones"""
        # Validaciones
        if not all([nombre_completo, email, password, confirm_password, nombre_negocio]):
            return False, "Todos los campos son obligatorios"
        
        if not self._validar_email(email):
            return False, "Formato de email inválido"
        
        if not self._validar_password(password):
            return False, "La contraseña debe tener al menos 6 caracteres"
        
        if password != confirm_password:
            return False, "Las contraseñas no coinciden"
        
        try:
            conn = db.get_connection()
            cursor = conn.cursor()
            
            # Verificar si el email ya existe
            if self.verificar_email_existente(email):
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
            
        except Exception as e:
            return False, f"Error al registrar usuario: {str(e)}"
    
    def login_usuario(self, email, password):
        """Valida las credenciales del usuario"""
        # Validaciones básicas
        if not email or not password:
            return False, "Email y contraseña son obligatorios"
        
        if not self._validar_email(email):
            return False, "Formato de email inválido"
        
        try:
            conn = db.get_connection()
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
                
        except Exception as e:
            return False, f"Error al iniciar sesión: {str(e)}"
    
    def verificar_email_existente(self, email):
        """Verifica si un email ya está registrado"""
        try:
            conn = db.get_connection()
            cursor = conn.cursor()
            
            cursor.execute("SELECT id FROM usuarios WHERE email = ?", (email,))
            existe = cursor.fetchone() is not None
            
            conn.close()
            return existe
            
        except Exception:
            return False

# Instancia global del servicio de autenticación
auth_service = AuthService()