class Usuario:
    def __init__(self, id=None, nombre_completo="", email="", password="", nombre_negocio="", fecha_creacion=""):
        self.id = id
        self.nombre_completo = nombre_completo
        self.email = email
        self.password = password
        self.nombre_negocio = nombre_negocio
        self.fecha_creacion = fecha_creacion
    
    def guardar(self):
        """Guardar usuario en la base de datos"""
        conn = db.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO usuarios (nombre_completo, email, password, nombre_negocio)
                VALUES (?, ?, ?, ?)
            ''', (self.nombre_completo, self.email, self.password, self.nombre_negocio))
            
            conn.commit()
            self.id = cursor.lastrowid
            return True
            
        except sqlite3.IntegrityError:
            # Email ya existe
            return False
        finally:
            conn.close()
    
    @staticmethod
    def buscar_por_email(email):
        """Buscar usuario por email"""
        conn = db.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM usuarios WHERE email = ?', (email,))
        usuario_data = cursor.fetchone()
        conn.close()
        
        if usuario_data:
            return Usuario(
                id=usuario_data['id'],
                nombre_completo=usuario_data['nombre_completo'],
                email=usuario_data['email'],
                password=usuario_data['password'],
                nombre_negocio=usuario_data['nombre_negocio'],
                fecha_creacion=usuario_data['fecha_creacion']
            )
        return None
    
    @staticmethod
    def validar_login(email, password):
        """Validar credenciales de login"""
        usuario = Usuario.buscar_por_email(email)
        if usuario and usuario.password == password:  # En producciÃ³n usar hashing!
            return usuario
        return None