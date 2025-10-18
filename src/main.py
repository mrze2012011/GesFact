"""
Punto de entrada principal de GesFact
Persona 3 - Versión básica para testing
"""
from src.database.database import db
from models.usuario import Usuario

def main():
    print("🚀 Iniciando GesFact...")
    print("✅ Base de datos configurada correctamente")
    print(f"📁 Base de datos ubicada en: {db.db_path}")
    
    # La base de datos ya se inicializó automáticamente
    # al importar db desde database.py
    
    input("Presiona Enter para salir...")

if __name__ == "__main__":
    main()
