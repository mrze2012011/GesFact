   
import customtkinter as ctk
from src.database.database import db
<<<<<<< HEAD
from models.usuario import Usuario
=======
from src.services.auth_service import inicializar_auth_service
from src.ui.login_window import LoginWindow
>>>>>>> e33858b4fd6f370900ef53c83f1d3a05cc4c7c6b

def main():
    print("🚀 Iniciando GesFact...")
    
    # Inicializar servicios
    inicializar_auth_service(db.db_path)
    print("✅ Servicio de autenticación inicializado")
    
    # Configurar CustomTkinter
    ctk.set_appearance_mode("System")  # "Light", "Dark", "System"
    ctk.set_default_color_theme("blue")  # Temas: "blue", "green", "dark-blue"
    
    print("✅ Base de datos configurada correctamente")
    print(f"📁 Base de datos ubicada en: {db.db_path}")
    
    # Iniciar aplicación con ventana de login
    print("🎨 Iniciando interfaz gráfica...")
    app = LoginWindow()
    app.mainloop()

if __name__ == "__main__":
    main()