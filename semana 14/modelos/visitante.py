
class Visitante:
    # Se inicializan los atributos principales del visitante: cédula, nombre y motivo.
    def __init__(self, cedula: str, nombre: str, motivo: str):
        self.cedula = cedula      # Se guarda la cédula como identificador único.
        self.nombre = nombre      # Se almacena el nombre completo del visitante.
        self.motivo = motivo      # Se registra el motivo de la visita.

    # Se implementa un metodo especial para devolver una representación en texto del objeto.
    def __str__(self):
        # Se construye una cadena legible que muestra la cédula, el nombre y el motivo.
        return f"{self.cedula} - {self.nombre} ({self.motivo})"

