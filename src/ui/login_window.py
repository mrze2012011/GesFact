import customtkinter as ctk
from src.services.auth_service import auth_service
from src.ui.registro_window import RegistroWindow

class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("GesFact - Inicio de Sesión")
        self.geometry("450x500")
        self.resizable(False, False)
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # ====== Estilo general ======
        self.configure(fg_color="#f5f6fa")  # fondo claro general

        # ====== Contenedor central ======
        self.main_frame = ctk.CTkFrame(self, corner_radius=15, fg_color="white")
        self.main_frame.pack(pady=80, padx=60, fill="both", expand=False)

        # ====== Título ======
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="Bienvenido a GesFact",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="#2f3640"
        )
        self.title_label.pack(pady=(25, 10))

        self.subtitle_label = ctk.CTkLabel(
            self.main_frame,
            text="Inicia sesión para continuar",
            font=ctk.CTkFont(size=14),
            text_color="#718093"
        )
        self.subtitle_label.pack(pady=(0, 20))

        # ====== Campos ======
        self.email_entry = ctk.CTkEntry(
            self.main_frame,
            placeholder_text="Correo electrónico",
            height=40,
            corner_radius=10
        )
        self.email_entry.pack(pady=10, padx=40)

        self.password_entry = ctk.CTkEntry(
            self.main_frame,
            placeholder_text="Contraseña",
            show="•",
            height=40,
            corner_radius=10
        )
        self.password_entry.pack(pady=10, padx=40)

        # ====== Botones ======
        self.login_button = ctk.CTkButton(
            self.main_frame,
            text="Iniciar Sesión",
            height=40,
            corner_radius=10,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#0078d7",
            hover_color="#005fa3",
            command=self._iniciar_sesion
        )
        self.login_button.pack(pady=(20, 10), padx=40, fill="x")

        self.register_button = ctk.CTkButton(
            self.main_frame,
            text="Crear cuenta",
            height=38,
            corner_radius=10,
            fg_color="white",
            text_color="#0078d7",
            border_width=2,
            border_color="#0078d7",
            hover_color="#f0f3f7",
            command=self._abrir_registro
        )
        self.register_button.pack(pady=(0, 15), padx=40, fill="x")

        # ====== Mensaje ======
        self.mensaje = ctk.CTkLabel(self.main_frame, text="", text_color="#e84118")
        self.mensaje.pack(pady=5)

    # ====== Lógica de login ======
    def _iniciar_sesion(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        exito, resultado = auth_service.login_usuario(email, password)
        if exito:
            self.mensaje.configure(text=f"✅ Bienvenido {resultado['nombre']}", text_color="#44bd32")
            self.after(1000, lambda: self._abrir_dashboard(resultado))  # ← aquí enviamos el usuario
            
        else:
            self.mensaje.configure(text=f"❌ {resultado}", text_color="#e84118")

    def _abrir_dashboard(self, usuario):
        from src.ui.dashboard_window import DashboardWindow
        self.withdraw()
        dashboard = DashboardWindow(usuario, self)
        dashboard.mainloop()


    # ====== Abrir registro ======
    def _abrir_registro(self):
        self.withdraw()
        registro = RegistroWindow(self)
        registro.mainloop()
