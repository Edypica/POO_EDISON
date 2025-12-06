class Animal:  # ( defino la clase llamada Animal)
    def mover(self):  # (aquí creo un metodo llamado mover dentro de la clase Animal)
        print("Me muevo")  # (cuando se ejecute, muestro en pantalla el mensaje "Me muevo")

class Gato(Animal):  # ( defino la clase Gato y heredo de Animal)
    pass  # (no agrego nada nuevo, simplemente heredo lo que ya tiene Animal)

g = Gato()  # (aquí creo un objeto llamado g a partir de la clase Gato)
g.mover()  # (aquí llamo al metodo mover que heredé de Animal y muestro )