import tkinter as tk
from tkinter import messagebox
from ui.register_window import RegisterWindow

class LoginWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PIA AFIs - Iniciar sesión")
        self.root.configure(bg="#e0e0e0")
        self.root.geometry("400x450")
        self.root.resizable(False, False)  # no permitir cambiar tamaño

        # Marco principal
        self.frame = tk.Frame(self.root, bg="#f5f5f5", bd=2, relief="ridge")
        self.frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=400)

        # Título
        tk.Label(self.frame, text="Iniciar Sesión", font=("Segoe UI", 20, "bold"), bg="#f5f5f5", fg="#333").pack(pady=20)

        # Campo usuario
        tk.Label(self.frame, text="Usuario (Matrícula)", bg="#f5f5f5", fg="#555", font=("Segoe UI", 11)).pack(pady=(10,0))
        self.username_entry = tk.Entry(self.frame, font=("Segoe UI", 11), justify="center")
        self.username_entry.pack(pady=5, ipady=6, ipadx=10)

        # Campo contraseña
        tk.Label(self.frame, text="Contraseña", bg="#f5f5f5", fg="#555", font=("Segoe UI", 11)).pack(pady=(10,0))
        self.password_entry = tk.Entry(self.frame, show="*", font=("Segoe UI", 11), justify="center")
        self.password_entry.pack(pady=5, ipady=6, ipadx=10)

        # Botón de ingresar
        self.login_btn = tk.Button(
            self.frame, text="Ingresar", bg="#777777", fg="white",
            font=("Segoe UI", 12, "bold"), relief="flat", cursor="hand2",
            activebackground="#555555", activeforeground="white",
            command=self.login_action
        )
        self.login_btn.pack(pady=20, ipadx=10, ipady=5)

        # Botón de registrarse
        self.register_btn = tk.Button(
            self.frame, text="Registrarse", bg="#cccccc", fg="#333",
            font=("Segoe UI", 11), relief="flat", cursor="hand2",
            activebackground="#bbbbbb",
            command=self.register_action
        )
        self.register_btn.pack(pady=5, ipadx=10, ipady=5)

        # Pie de página
        tk.Label(self.frame, text="© 2025 Sistema AFIs", bg="#f5f5f5", fg="#999", font=("Segoe UI", 9)).pack(side="bottom", pady=10)

        self.root.mainloop()

    # --- Acciones de botones ---
    def login_action(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "" or password == "":
            messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
        else:
            messagebox.showinfo("Inicio de sesión", f"Bienvenido, {username}")

    def register_action(self):
        RegisterWindow()
