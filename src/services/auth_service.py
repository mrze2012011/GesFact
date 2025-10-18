from src.database.database import db

class AuthService:
    def __init__(self, db_instance):
        self.db = db_instance

    # 🔹 Registrar nuevo usuario
    def registrar_usuario(self, nombre, email, password):
        # Verificar si ya existe
        usuario = self.db.obtener_usuario_por_email(email)
        if usuario:
            return False, "El correo ya está registrado."

        # Insertar usuario nuevo
        self.db.insertar_usuario(nombre, email, password)
        return True, "Usuario registrado correctamente."

    # 🔹 Iniciar sesión
    def login_usuario(self, email, password):
        usuario = self.db.obtener_usuario_por_email(email)
        if not usuario:
            return False, "El correo no está registrado."

        if usuario["password"] != password:
            return False, "Contraseña incorrecta."

        return True, usuario  # Retorna el diccionario con los datos del usuario


# Instancia global (ya inicializada con la base de datos actual)
auth_service = AuthService(db)
