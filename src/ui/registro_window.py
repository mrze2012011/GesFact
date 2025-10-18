import customtkinter as ctk
from src.services.auth_service import auth_service

class RegistroWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Crear cuenta")
        self.geometry("400x400")
        self.parent = parent  # Guardamos la ventana de login

        ctk.CTkLabel(self, text="Registro de usuario", font=("Arial", 18)).pack(pady=20)
        self.nombre_entry = ctk.CTkEntry(self, placeholder_text="Nombre completo")
        self.nombre_entry.pack(pady=10)
        self.email_entry = ctk.CTkEntry(self, placeholder_text="Correo electrónico")
        self.email_entry.pack(pady=10)
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Contraseña", show="*")
        self.password_entry.pack(pady=10)

        ctk.CTkButton(self, text="Registrar", command=self._registrar_usuario).pack(pady=10)
        ctk.CTkButton(self, text="Volver", command=self._volver_login).pack(pady=5)

        self.mensaje = ctk.CTkLabel(self, text="")
        self.mensaje.pack(pady=10)

    def _registrar_usuario(self):
        nombre = self.nombre_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        exito, resultado = auth_service.registrar_usuario(nombre, email, password)
        if exito:
            self.mensaje.configure(text="✅ Cuenta creada correctamente.")
            self.after(1500, self._volver_login)
        else:
            self.mensaje.configure(text=f"❌ {resultado}")

    def _volver_login(self):
        self.destroy()
        self.parent.deiconify()  # Muestra de nuevo la ventana de login
