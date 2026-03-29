from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import ListaTareasApp

if __name__ == "__main__":
    servicio = TareaServicio()       # Instancia la lógica de negocio
    app = ListaTareasApp(servicio)   # Pasa el servicio a la interfaz
    app.run()                        # Arranca la aplicación
