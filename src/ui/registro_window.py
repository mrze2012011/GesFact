import customtkinter as ctk

class RegistroWindow(ctk.CTkToplevel):
    def __init__(self, parent, navigation_callback=None):
        super().__init__(parent)
        
        self.parent = parent
        self.navigation_callback = navigation_callback
        self.title("GesFact - Crear Cuenta")
        self.geometry("400x600")
        self.resizable(False, False)
        
        self.grid_columnconfigure(0, weight=1)
        self._crear_widgets()
        
        self.transient(parent)
        self.grab_set()
    
    def _crear_widgets(self):
        # Logo
        self.logo_label = ctk.CTkLabel(
            self, 
            text="GesFact", 
            font=ctk.CTkFont(size=32, weight="bold")
        )
        self.logo_label.grid(row=0, column=0, pady=(40, 20))
        
        # Frame del formulario
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.grid(row=1, column=0, padx=50, pady=20, sticky="nsew")
        
        campos = [
            ("Nombre Completo", "text"),
            ("Email", "email"),
            ("Contraseña", "password"),
            ("Confirmar Contraseña", "password"),
            ("Nombre del Negocio", "text")
        ]
        
        self.entries = {}
        for i, (label, tipo) in enumerate(campos):
            lbl = ctk.CTkLabel(self.form_frame, text=label + ":")
            lbl.grid(row=i*2, column=0, padx=20, pady=(20 if i==0 else 15, 5), sticky="w")
            
            show_char = "•" if tipo == "password" else ""
            entry = ctk.CTkEntry(
                self.form_frame, 
                placeholder_text=f"Ingresa tu {label.lower()}",
                show=show_char
            )
            entry.grid(row=i*2+1, column=0, padx=20, pady=(0, 0), sticky="ew")
            self.entries[label] = entry
        
        self.registro_button = ctk.CTkButton(
            self.form_frame, 
            text="Crear Cuenta",
            command=self._crear_cuenta
        )
        self.registro_button.grid(row=10, column=0, padx=20, pady=30)
    
    def _crear_cuenta(self):
        datos = {
            'nombre': self.entries['Nombre Completo'].get(),
            'email': self.entries['Email'].get(),
            'password': self.entries['Contraseña'].get(),
            'confirm_password': self.entries['Confirmar Contraseña'].get(),
            'negocio': self.entries['Nombre del Negocio'].get()
        }
        
        # TODO: Validar datos y conectar con auth_service
        print("Datos registro:", datos)
        
        if all(datos.values()):
            if self.navigation_callback:
                self.navigation_callback('login')
            else:
                self.destroy()
                self.parent.deiconify()
    
    def destroy(self):
        if self.parent:
            self.parent.deiconify()
        super().destroy()