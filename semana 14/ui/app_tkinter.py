import tkinter as tk
from tkinter import ttk, messagebox

# Se define la clase encargada de construir la interfaz gráfica con Tkinter.
class AppTkinter:
    def __init__(self, servicio):
        # Se recibe el servicio como dependencia para manejar la lógica CRUD.
        self.servicio = servicio
        self.root = tk.Tk()
        self.root.title("Registro de Visitantes")

        # --- Formulario ---
        # Se crean etiquetas y campos de entrada para capturar los datos del visitante.
        tk.Label(self.root, text="Cédula").grid(row=0, column=0)
        self.entry_cedula = tk.Entry(self.root)
        self.entry_cedula.grid(row=0, column=1)

        tk.Label(self.root, text="Nombre").grid(row=1, column=0)
        self.entry_nombre = tk.Entry(self.root)
        self.entry_nombre.grid(row=1, column=1)

        tk.Label(self.root, text="Motivo").grid(row=2, column=0)
        self.entry_motivo = tk.Entry(self.root)
        self.entry_motivo.grid(row=2, column=1)

        # --- Botones ---
        # Se agregan botones para registrar, eliminar y limpiar campos del formulario.
        tk.Button(self.root, text="Registrar", command=self.registrar).grid(row=3, column=0)
        tk.Button(self.root, text="Eliminar", command=self.eliminar).grid(row=3, column=1)
        tk.Button(self.root, text="Limpiar Campos", command=self.limpiar_campos).grid(row=3, column=2)

        # --- Tabla ---
        # Se construye una tabla dinámica para mostrar los registros actuales.
        self.tree = ttk.Treeview(self.root, columns=("cedula", "nombre", "motivo"), show="headings")
        self.tree.heading("cedula", text="Cédula")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("motivo", text="Motivo")
        self.tree.grid(row=4, column=0, columnspan=3)

    # Se implementa el método para registrar un visitante desde los campos de entrada.
    def registrar(self):
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        motivo = self.entry_motivo.get()

        # Se valida la información y se muestra un mensaje de éxito o advertencia.
        if self.servicio.registrar(cedula, nombre, motivo):
            messagebox.showinfo("Éxito", "Visitante registrado")
            self.actualizar_tabla()
            self.limpiar_campos()
        else:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")

    # Se implementa el método para eliminar un visitante seleccionado en la tabla.
    def eliminar(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            cedula = self.tree.item(seleccionado)["values"][0]
            if self.servicio.eliminar(cedula):
                messagebox.showinfo("Éxito", "Visitante eliminado")
                self.actualizar_tabla()
        else:
            messagebox.showwarning("Error", "Seleccione un visitante")

    # Se limpian los campos del formulario después de cada acción.
    def limpiar_campos(self):
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_motivo.delete(0, tk.END)

    # Se actualiza la tabla para reflejar los registros actuales.
    def actualizar_tabla(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for v in self.servicio.listar():
            self.tree.insert("", tk.END, values=(v.cedula, v.nombre, v.motivo))

    # Se inicia el ciclo principal de la aplicación gráfica.
    def run(self):
        self.root.mainloop()
