class Perro:  # (defino la clase Perro)
    def sonido(self):  # (creo el metodo sonido)
        print("Guau")  # (muestro Guau)

class Gato:  # (defino la clase Gato)
    def sonido(self):  # (creo el metodo sonido)
        print("Miau")  # (muestro Miau)

def hacer_sonido(animal):  # (defino función que recibe un animal)
    animal.sonido()  # (llamo al sonido)

hacer_sonido(Perro())  # (ejecuto sonido del Perro)
hacer_sonido(Gato())  # (ejecuto sonido del Gato)