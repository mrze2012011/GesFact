import customtkinter as ctk

class DashboardWindow(ctk.CTk):
    def __init__(self, usuario, login_window=None):
        super().__init__()
        self.usuario = usuario
        self.login_window = login_window
        self.title("GesFact - Panel Principal")
        self.geometry("900x600")
        self.minsize(700, 500)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        self.configure(fg_color="#f5f6fa")

        # Configurar diseño responsive
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ===== Menú lateral =====
        sidebar = ctk.CTkFrame(self, fg_color="#ffffff", corner_radius=0)
        sidebar.grid(row=0, column=0, sticky="nswe")
        sidebar.grid_rowconfigure(6, weight=1)  # espacio flexible

        logo = ctk.CTkLabel(sidebar, text="🧾 GesFact", font=ctk.CTkFont(size=20, weight="bold"))
        logo.grid(row=0, column=0, pady=(20, 10), padx=20)

        ctk.CTkButton(sidebar, text="Ventas", width=160, height=35, corner_radius=8).grid(row=1, column=0, pady=5, padx=20)
        ctk.CTkButton(sidebar, text="Clientes", width=160, height=35, corner_radius=8).grid(row=2, column=0, pady=5, padx=20)
        ctk.CTkButton(sidebar, text="Productos", width=160, height=35, corner_radius=8).grid(row=3, column=0, pady=5, padx=20)
        ctk.CTkButton(sidebar, text="Reportes", width=160, height=35, corner_radius=8).grid(row=4, column=0, pady=5, padx=20)

        ctk.CTkButton(
            sidebar, text="Cerrar sesión", fg_color="#e84118", hover_color="#c23616",
            command=self._cerrar_sesion
        ).grid(row=5, column=0, pady=20, padx=20)

        # ===== Contenedor principal =====
        main_content = ctk.CTkFrame(self, fg_color="white", corner_radius=15)
        main_content.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        main_content.grid_columnconfigure(0, weight=1)
        main_content.grid_rowconfigure(1, weight=1)

        # Título superior
        title_label = ctk.CTkLabel(
            main_content,
            text=f"Bienvenido, {self.usuario['nombre']}",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="#2f3640"
        )
        title_label.grid(row=0, column=0, pady=(20, 10))

        # Área dinámica
        self.dashboard_frame = ctk.CTkFrame(main_content, fg_color="#f9fafc", corner_radius=10)
        self.dashboard_frame.grid(row=1, column=0, sticky="nsew", padx=15, pady=15)
        self.dashboard_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.dashboard_frame.grid_rowconfigure(0, weight=1)

        # ===== Widgets de ejemplo =====
        cards = [
            ("Ventas del día", "45", "#00a8ff"),
            ("Clientes activos", "12", "#9c88ff"),
            ("Productos en stock", "230", "#4cd137")
        ]

        for i, (titulo, valor, color) in enumerate(cards):
            card = ctk.CTkFrame(self.dashboard_frame, corner_radius=12, fg_color=color)
            card.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")
            ctk.CTkLabel(card, text=titulo, font=ctk.CTkFont(size=15, weight="bold"), text_color="white").pack(pady=(20, 5))
            ctk.CTkLabel(card, text=valor, font=ctk.CTkFont(size=30, weight="bold"), text_color="white").pack()

    def _cerrar_sesion(self):
        """Regresar a la ventana de login"""
        self.destroy()
        if self.login_window:
            self.login_window.deiconify()
