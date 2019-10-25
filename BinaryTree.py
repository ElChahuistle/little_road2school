# Incluimos el paquete "math" para poder usar la función "ceil", la cual devuelve el valor
# del entero inmediato superior al número que se pasa como parámetro.
import math


class BinaryTree(list):
    # Nuevamente, vamos a crear una clase que hereda de la clase "list". Expresamente usaremos número para
    # simplificar el uso del árbol.

    # Constructor de la clase que inicializa la clase "list" de la que hereda.
    # Como en Stack y Queue, el constructor recibe un parámetro el cual será un árbol inicial.
    def __init__(self, tree=None):
        self.root = None

        if tree is None:
            super().__init__(list())
        else:
            self.root = math.floor(len(tree) / 2)
            super().__init__(tree)

    def add_number(self, number: int):
        if len(self) == 0:
            self.root = 0
            self.append(number)
        else:
            while 0 <= self.root < len(self):
                if self[self.root] <= number:
                    self.root = math.floor((self.root - 1) / 2)
