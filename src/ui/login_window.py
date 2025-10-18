import customtkinter as ctk
from src.services.auth_service import auth_service
from src.ui.registro_window import RegistroWindow
from tkinter import messagebox
from src.ui.dashboard_window import DashboardWindow  # ✅ Import del dashboard


class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Inicio de sesión - GesFact")
        self.geometry("400x350")

        ctk.CTkLabel(self, text="Iniciar Sesión", font=("Arial", 18)).pack(pady=20)
        self.email_entry = ctk.CTkEntry(self, placeholder_text="Correo electrónico")
        self.email_entry.pack(pady=10)
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Contraseña", show="*")
        self.password_entry.pack(pady=10)

        ctk.CTkButton(self, text="Iniciar sesión", command=self._iniciar_sesion).pack(pady=10)
        ctk.CTkButton(self, text="Crear cuenta", command=self._abrir_registro).pack(pady=5)

        self.mensaje = ctk.CTkLabel(self, text="")
        self.mensaje.pack(pady=10)

    def _iniciar_sesion(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        exito, resultado = auth_service.login_usuario(email, password)

        if exito:
            # Muestra mensaje y abre el dashboard
            messagebox.showinfo("Éxito", f"Bienvenido {resultado['nombre']}")
            self.destroy()  # Cierra la ventana de login
            dashboard = DashboardWindow(resultado)
            dashboard.mainloop()
        else:
            self.mensaje.configure(text=f"❌ {resultado}")

    def _abrir_registro(self):
        # Abrir la ventana de registro sin cerrar el login
        self.withdraw()  # Oculta la ventana de login
        registro = RegistroWindow(self)
        registro.mainloop()
