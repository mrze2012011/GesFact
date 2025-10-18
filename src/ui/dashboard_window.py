import customtkinter as ctk

class DashboardWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("GesFact - Dashboard")
        self.geometry("800x600")
        
        # Configurar grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        self._crear_header()
        self._crear_contenido()
    
    def _crear_header(self):
        # Header con logo e icono de usuario
        self.header_frame = ctk.CTkFrame(self, height=60)
        self.header_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
        self.header_frame.grid_columnconfigure(0, weight=1)
        
        # Logo izquierda
        self.logo_header = ctk.CTkLabel(
            self.header_frame, 
            text="GesFact", 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.logo_header.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        
        # Icono usuario derecha
        self.user_icon = ctk.CTkButton(
            self.header_frame,
            text="👤",
            width=40,
            height=40,
            fg_color="transparent",
            hover_color="#2b2b2b"
        )
        self.user_icon.grid(row=0, column=1, padx=20, pady=10, sticky="e")
    
    def _crear_contenido(self):
        # Contenido principal
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(1, weight=1)
        
        # Logo grande en el centro
        self.logo_central = ctk.CTkLabel(
            self.content_frame, 
            text="GesFact", 
            font=ctk.CTkFont(size=48, weight="bold")
        )
        self.logo_central.grid(row=0, column=0, pady=(100, 50))
        
        # Frame para botones
        self.botones_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        self.botones_frame.grid(row=1, column=0, pady=(0, 100))
        
        # Botones de secciones
        botones = [
            "Facturación",
            "Clientes", 
            "Gastos",
            "Reportes",
            "Configuración"
        ]
        
        for i, texto in enumerate(botones):
            btn = ctk.CTkButton(
                self.botones_frame,
                text=texto,
                width=150,
                height=40,
                state="normal"  # Cambiar a "disabled" temporalmente
            )
            btn.grid(row=i//3, column=i%3, padx=10, pady=10)