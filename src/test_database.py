from src.database.database import db

def test_database():
    """Probar que la base de datos se crea correctamente"""
    print("🧪 Probando base de datos...")
    
    # La base de datos se inicializa automáticamente
    conn = db.get_connection()
    cursor = conn.cursor()
    
    # Verificar que la tabla usuarios existe
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='usuarios'")
    tabla_existe = cursor.fetchone()
    
    if tabla_existe:
        print("✅ Tabla 'usuarios' creada correctamente")
    else:
        print("❌ Error: Tabla 'usuarios' no existe")
    
    conn.close()

if __name__ == "__main__":
    test_database()