import customtkinter as ctk
from .registro_window import RegistroWindow

class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("GesFact - Iniciar Sesión")
        self.geometry("400x500")
        self.resizable(False, False)
        
        # Configurar grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        self._crear_widgets()
    
    def _crear_widgets(self):
        # Logo grande
        self.logo_label = ctk.CTkLabel(
            self, 
            text="GesFact", 
            font=ctk.CTkFont(size=36, weight="bold")
        )
        self.logo_label.grid(row=0, column=0, pady=(50, 30))
        
        # Frame del formulario
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.grid(row=1, column=0, padx=50, pady=20, sticky="nsew")
        
        # Email
        self.email_label = ctk.CTkLabel(self.form_frame, text="Email:")
        self.email_label.grid(row=0, column=0, padx=20, pady=(30, 5), sticky="w")
        
        self.email_entry = ctk.CTkEntry(self.form_frame, placeholder_text="tu@email.com")
        self.email_entry.grid(row=1, column=0, padx=20, pady=(0, 15), sticky="ew")
        
        # Contraseña
        self.password_label = ctk.CTkLabel(self.form_frame, text="Contraseña:")
        self.password_label.grid(row=2, column=0, padx=20, pady=(0, 5), sticky="w")
        
        self.password_entry = ctk.CTkEntry(self.form_frame, placeholder_text="••••••••", show="•")
        self.password_entry.grid(row=3, column=0, padx=20, pady=(0, 30), sticky="ew")
        
        # Botón iniciar sesión
        self.login_button = ctk.CTkButton(
            self.form_frame, 
            text="Iniciar Sesión",
            command=self._iniciar_sesion
        )
        self.login_button.grid(row=4, column=0, padx=20, pady=(0, 20))
        
        # Texto y botón crear cuenta
        self.registro_label = ctk.CTkLabel(self.form_frame, text="¿No tienes cuenta?")
        self.registro_label.grid(row=5, column=0, padx=20, pady=(0, 5))
        
        self.registro_button = ctk.CTkButton(
            self.form_frame, 
            text="Crear cuenta",
            command=self._abrir_registro,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE")
        )
        self.registro_button.grid(row=6, column=0, padx=20, pady=(0, 30))
    
    def _iniciar_sesion(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        # TODO: Conectar con auth_service
        print(f"Login attempt: {email}, {password}")
        
        # Simulación de login exitoso
        if email and password:
            from .dashboard_window import DashboardWindow
            self.destroy()
            dashboard = DashboardWindow()
            dashboard.mainloop()
    
    def _abrir_registro(self):
        self.withdraw()  # Oculta ventana login
        registro_window = RegistroWindow(self)
        registro_window.mainloop()