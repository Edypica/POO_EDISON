class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre  # Guardo el nombre como privado

    def mostrar(self):
        print(self.__nombre)  # Lo muestro con un método

p = Persona("Ana")
p.mostrar()  #Imprimimos