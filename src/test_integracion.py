"""
Pruebas de integración para GesFact
"""
import sys
import os

# Agregar src al path para los imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from database.database import db
from services.auth_service import auth_service

def test_database():
    """Prueba la conexión a la base de datos"""
    print("🧪 Probando base de datos...")
    try:
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        conn.close()
        
        print(f"✅ Tablas en la base de datos: {[table[0] for table in tables]}")
        return True
    except Exception as e:
        print(f"❌ Error en base de datos: {e}")
        return False

def test_auth_service():
    """Prueba el servicio de autenticación"""
    print("\n🧪 Probando servicio de autenticación...")
    
    # Test 1: Registrar usuario
    print("1. Probando registro de usuario...")
    success, message = auth_service.registrar_usuario(
        "Juan Pérez", 
        "juan@test.com", 
        "password123", 
        "password123", 
        "Mi Negocio"
    )
    print(f"   Registro: {'✅' if success else '❌'} {message}")
    
    # Test 2: Verificar email existente
    print("2. Probando verificación de email...")
    existe = auth_service.verificar_email_existente("juan@test.com")
    print(f"   Email existe: {'✅' if existe else '❌'}")
    
    # Test 3: Login exitoso
    print("3. Probando login exitoso...")
    success, result = auth_service.login_usuario("juan@test.com", "password123")
    print(f"   Login exitoso: {'✅' if success else '❌'} {result}")
    
    # Test 4: Login fallido
    print("4. Probando login fallido...")
    success, result = auth_service.login_usuario("juan@test.com", "wrongpassword")
    print(f"   Login fallido: {'✅' if not success else '❌'} {result}")
    
    return True

def test_validaciones():
    """Prueba las validaciones del auth_service"""
    print("\n🧪 Probando validaciones...")
    
    # Test: Email inválido
    success, message = auth_service.registrar_usuario(
        "Test", "email-invalido", "pass", "pass", "Negocio"
    )
    print(f"✅ Validación email: {'❌' if not success else '⚠️'} {message}")
    
    # Test: Contraseña corta
    success, message = auth_service.registrar_usuario(
        "Test", "test@test.com", "123", "123", "Negocio"
    )
    print(f"✅ Validación contraseña: {'❌' if not success else '⚠️'} {message}")
    
    # Test: Campos vacíos
    success, message = auth_service.registrar_usuario("", "", "", "", "")
    print(f"✅ Validación campos vacíos: {'❌' if not success else '⚠️'} {message}")

if __name__ == "__main__":
    print("🚀 INICIANDO PRUEBAS DE GESFACT")
    print("=" * 50)
    
    # Ejecutar pruebas
    test_database()
    test_auth_service() 
    test_validaciones()
    
    print("\n" + "=" * 50)
    print("📊 PRUEBAS COMPLETADAS")
    print("💡 Ejecuta 'python main.py' para probar la interfaz gráfica")