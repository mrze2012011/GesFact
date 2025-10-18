import customtkinter as ctk
from src.services.auth_service import auth_service
from src.ui.login_window import LoginWindow

def main():
    print("🚀 Iniciando GesFact...")

    # Configurar CustomTkinter
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    print("✅ Servicio de autenticación inicializado")
    print("✅ Base de datos configurada correctamente")
    
    # Iniciar aplicación con ventana de login
    print("🎨 Iniciando interfaz gráfica...")
    app = LoginWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
