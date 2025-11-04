import tkinter as tk
from tkinter import messagebox

class RegisterWindow:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Registro de Usuario")
        self.root.geometry("700x350")
        self.root.resizable(False, False)
        self.root.configure(bg="#e0e0e0")

        # Tipo de usuario
        tk.Label(self.root, text="Selecciona el tipo de usuario:", bg="#e0e0e0", fg="#333", font=("Segoe UI", 11)).pack(pady=10)
        self.user_type_var = tk.StringVar(value="student")
        options_frame = tk.Frame(self.root, bg="#e0e0e0")
        options_frame.pack()

        tk.Radiobutton(options_frame, text="Alumno", variable=self.user_type_var, value="student", bg="#e0e0e0", font=("Segoe UI", 11), command=self.update_form).pack(side="left", padx=15)
        tk.Radiobutton(options_frame, text="Administrador", variable=self.user_type_var, value="admin", bg="#e0e0e0", font=("Segoe UI", 11), command=self.update_form).pack(side="left", padx=15)
        tk.Radiobutton(options_frame, text="Facultad", variable=self.user_type_var, value="faculty", bg="#e0e0e0", font=("Segoe UI", 11), command=self.update_form).pack(side="left", padx=15)

        # Frame de formulario
        self.form_frame = tk.Frame(self.root, bg="#f5f5f5", bd=2, relief="ridge")
        self.form_frame.place(relx=0.5, rely=0.6, anchor="center", width=650, height=250)

        self.entries = {}
        self.update_form()  # mostrar formulario inicial

    def update_form(self):
        # Limpiar frame
        for widget in self.form_frame.winfo_children():
            widget.destroy()
        self.entries.clear()

        user_type = self.user_type_var.get()

        # Columnas horizontales
        col1 = tk.Frame(self.form_frame, bg="#f5f5f5")
        col1.pack(side="left", padx=20, pady=20)
        col2 = tk.Frame(self.form_frame, bg="#f5f5f5")
        col2.pack(side="left", padx=20, pady=20)

        row = 0
        # Campos comunes
        labels = ["Nombre", "Apellido Paterno", "Apellido Materno", "Matrícula", "Contraseña"]
        for i, label in enumerate(labels):
            tk.Label(col1 if i < 3 else col2, text=label, bg="#f5f5f5", fg="#333", font=("Segoe UI", 10)).grid(row=i%3, column=0, pady=5, sticky="w")
            entry = tk.Entry(col1 if i < 3 else col2, font=("Segoe UI", 10))
            entry.grid(row=i%3, column=1, pady=5, padx=5)
            self.entries[label.lower().replace(" ", "_")] = entry

        # Campos específicos
        if user_type == "student":
            tk.Label(col1, text="Facultad ID", bg="#f5f5f5", fg="#333", font=("Segoe UI", 10)).grid(row=3, column=0, pady=5, sticky="w")
            faculty_entry = tk.Entry(col1, font=("Segoe UI", 10))
            faculty_entry.grid(row=3, column=1, pady=5, padx=5)
            self.entries["faculty_id"] = faculty_entry

            tk.Label(col1, text="Carrera ID", bg="#f5f5f5", fg="#333", font=("Segoe UI", 10)).grid(row=4, column=0, pady=5, sticky="w")
            career_entry = tk.Entry(col1, font=("Segoe UI", 10))
            career_entry.grid(row=4, column=1, pady=5, padx=5)
            self.entries["career_id"] = career_entry

        elif user_type == "admin":
            tk.Label(col1, text="Código Admin", bg="#f5f5f5", fg="#333", font=("Segoe UI", 10)).grid(row=3, column=0, pady=5, sticky="w")
            code_entry = tk.Entry(col1, font=("Segoe UI", 10), show="*")
            code_entry.grid(row=3, column=1, pady=5, padx=5)
            self.entries["code"] = code_entry

        elif user_type == "faculty":
            tk.Label(col1, text="Código Facultad", bg="#f5f5f5", fg="#333", font=("Segoe UI", 10)).grid(row=3, column=0, pady=5, sticky="w")
            code_entry = tk.Entry(col1, font=("Segoe UI", 10), show="*")
            code_entry.grid(row=3, column=1, pady=5, padx=5)
            self.entries["code"] = code_entry

        # Botón registrar
        register_btn = tk.Button(self.form_frame, text="Registrar", bg="#777777", fg="white", font=("Segoe UI", 11, "bold"),
                                 relief="flat", cursor="hand2", activebackground="#555555", activeforeground="white",
                                 command=self.register_user)
        register_btn.pack(side="bottom", pady=10, ipadx=10, ipady=5)

    def register_user(self):
        messagebox.showinfo("Registro", "Aquí se implementará el registro en la base de datos")
