import customtkinter as ctk
from tkinter import messagebox

class DashboardWindow(ctk.CTk):
    def __init__(self, usuario):
        super().__init__()
        self.title("GesFact - Panel Principal")
        self.geometry("900x600")

        # Mensaje de bienvenida
        label = ctk.CTkLabel(self, text=f"Bienvenido, {usuario['nombre']}", font=("Arial", 22, "bold"))
        label.pack(pady=30)

        # Botones de ejemplo
        btn_ventas = ctk.CTkButton(self, text="Registrar Venta", command=self._registrar_venta)
        btn_ventas.pack(pady=10)

        btn_clientes = ctk.CTkButton(self, text="Ver Clientes", command=self._ver_clientes)
        btn_clientes.pack(pady=10)

        btn_salir = ctk.CTkButton(self, text="Cerrar Sesión", fg_color="red", command=self._cerrar_sesion)
        btn_salir.pack(pady=20)

    def _registrar_venta(self):
        messagebox.showinfo("Registrar Venta", "Aquí podrás registrar una nueva venta.")

    def _ver_clientes(self):
        messagebox.showinfo("Clientes", "Aquí se mostraría la lista de clientes.")

    def _cerrar_sesion(self):
        from src.ui.login_window import LoginWindow
        self.destroy()
        login = LoginWindow()
        login.mainloop()
