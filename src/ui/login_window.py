import customtkinter as ctk
from src.services.auth_service import auth_service
from src.ui.registro_window import RegistroWindow
from tkinter import messagebox

class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("GesFact - Inicio de Sesión")
        self.geometry("500x550")
        self.minsize(400, 450)
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # ====== Fondo general ======
        self.configure(fg_color="#f5f6fa")

        # ====== Frame principal ======
        self.main_frame = ctk.CTkFrame(self, corner_radius=15, fg_color="white")
        self.main_frame.pack(expand=True, fill="both", padx=40, pady=40)

        # ====== Título ======
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="Bienvenido a GesFact",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="#2f3640"
        )
        self.title_label.pack(pady=(30, 5))

        self.subtitle_label = ctk.CTkLabel(
            self.main_frame,
            text="Inicia sesión para continuar",
            font=ctk.CTkFont(size=14),
            text_color="#718093"
        )
        self.subtitle_label.pack(pady=(0, 20))

        # ====== Entradas ======
        self.email_entry = ctk.CTkEntry(
            self.main_frame,
            placeholder_text="Correo electrónico",
            height=40,
            corner_radius=10
        )
        self.email_entry.pack(pady=10, padx=50, fill="x")

        self.password_entry = ctk.CTkEntry(
            self.main_frame,
            placeholder_text="Contraseña",
            show="•",
            height=40,
            corner_radius=10
        )
        self.password_entry.pack(pady=10, padx=50, fill="x")

        # ====== Mensaje dinámico ======
        self.mensaje = ctk.CTkLabel(self.main_frame, text="", text_color="#e84118")
        self.mensaje.pack(pady=(5, 10))

        # ====== Botón Login ======
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
        self.login_button.pack(pady=(10, 5), padx=50, fill="x")

        # ====== Botón Registro ======
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
        self.register_button.pack(pady=(0, 15), padx=50, fill="x")

        # ====== Footer ======
        self.footer_label = ctk.CTkLabel(
            self.main_frame,
            text="© 2025 GesFact - Sistema de Gestión de Facturación",
            font=ctk.CTkFont(size=12),
            text_color="#a4b0be"
        )
        self.footer_label.pack(pady=(20, 5))

        # ====== Evento de resize ======
        self.bind("<Configure>", self._on_resize)

    # ====== Lógica de Login ======
    def _iniciar_sesion(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        if not email or not password:
            self._mostrar_mensaje("Por favor ingresa tu correo y contraseña.", "#e84118")
            return

        exito, resultado = auth_service.login_usuario(email, password)

        if exito:
            self._mostrar_mensaje(f"✅ Bienvenido {resultado['nombre']}", "#44bd32")
            self.after(1000, lambda: self._abrir_dashboard(resultado))
        else:
            self._mostrar_mensaje(f"❌ {resultado}", "#e84118")

    # ====== Mostrar mensajes de alerta ======
    def _mostrar_mensaje(self, texto, color):
        self.mensaje.configure(text=texto, text_color=color)
        self.mensaje.pack()
        self.after(3000, lambda: self.mensaje.configure(text=""))  # se limpia después de 3s

    # ====== Abrir dashboard ======
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

    # ====== Adaptar a tamaño de ventana ======
    def _on_resize(self, event):
        width = event.width
        if width < 420:
            self.title_label.configure(font=ctk.CTkFont(size=18, weight="bold"))
        else:
            self.title_label.configure(font=ctk.CTkFont(size=22, weight="bold"))
