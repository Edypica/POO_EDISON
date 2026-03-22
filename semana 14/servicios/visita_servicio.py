from modelos.visitante import Visitante

# Se define la clase encargada de manejar la lógica CRUD de los visitantes.
class VisitaServicio:
    def __init__(self):
        # Se inicializa una lista privada para almacenar los objetos Visitante.
        self._visitantes = []  # Encapsulado

    # Se implementa el metodo para registrar un nuevo visitante.
    def registrar(self, cedula: str, nombre: str, motivo: str):
        # Se valida que todos los campos tengan información antes de crear el objeto.
        if not cedula or not nombre or not motivo:
            return False
        # Se instancia un nuevo objeto Visitante con los datos recibidos.
        visitante = Visitante(cedula, nombre, motivo)
        # Se agrega el visitante a la lista interna.
        self._visitantes.append(visitante)
        return True

    # Se devuelve la lista completa de visitantes registrados.
    def listar(self):
        return self._visitantes

    # Se elimina un visitante de la lista según su cédula.
    def eliminar(self, cedula: str):
        for v in self._visitantes:
            if v.cedula == cedula:
                # Se remueve el visitante encontrado.
                self._visitantes.remove(v)
                return True
        return False

    # Se limpia la lista de visitantes, dejándola vacía.
    def limpiar(self):
        self._visitantes.clear()

