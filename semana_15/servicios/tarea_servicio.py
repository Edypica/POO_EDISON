from modelos.tarea import Tarea

class TareaServicio:
    def __init__(self):
        self.tareas = {}

    def agregar(self, id, descripcion):
        tarea = Tarea(id, descripcion)
        self.tareas[id] = tarea

    def completar(self, id):
        if id in self.tareas:
            self.tareas[id].completada = True

    def eliminar(self, id):
        if id in self.tareas:
            del self.tareas[id]
