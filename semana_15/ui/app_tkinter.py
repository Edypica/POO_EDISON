import tkinter as tk
from tkinter import ttk

class ListaTareasApp:
    def __init__(self, servicio):
        self.servicio = servicio
        self.root = tk.Tk()
        self.root.title("Lista de Tareas")

        # Entrada de texto
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)

        # Botones visibles
        tk.Button(self.root, text="Añadir Tarea", command=self.add_tarea).pack(pady=2)
        tk.Button(self.root, text="Marcar Completada", command=self.marcar_completada).pack(pady=2)
        tk.Button(self.root, text="Eliminar", command=self.eliminar_tarea).pack(pady=2)

        # Treeview para mostrar tareas
        self.tree = ttk.Treeview(self.root, columns=("desc"), show="headings")
        self.tree.heading("desc", text="Descripción")
        self.tree.pack(pady=5)

        # Eventos
        self.entry.bind("<Return>", lambda e: self.add_tarea())       # Enter añade tarea
        self.tree.bind("<Double-1>", lambda e: self.marcar_completada())  # Doble clic completa

    def add_tarea(self):
        desc = self.entry.get()
        if desc:
            id = len(self.servicio.tareas) + 1
            self.servicio.agregar(id, desc)
            self.tree.insert("", "end", iid=id, values=(desc,))
            self.entry.delete(0, tk.END)

    def marcar_completada(self):
        seleccion = self.tree.selection()
        if seleccion:
            item = seleccion[0]
            self.servicio.completar(int(item))
            desc = self.servicio.tareas[int(item)].descripcion + " [Hecho]"
            self.tree.item(item, values=(desc,), tags="done")
            self.tree.tag_configure("done", foreground="gray")  # Feedback visual

    def eliminar_tarea(self):
        seleccion = self.tree.selection()
        if seleccion:
            item = seleccion[0]
            self.servicio.eliminar(int(item))
            self.tree.delete(item)

    def run(self):
        self.root.mainloop()
