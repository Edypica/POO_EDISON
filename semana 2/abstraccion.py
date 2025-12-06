class Animal:
    def sonido(self):  # Defino un método general
        pass  # No digo cómo, solo que existe

class Perro(Animal):
    def sonido(self):
        print("Guau")  # Aquí sí digo el sonido

Perro().sonido()  # Llamo y escucho el sonido