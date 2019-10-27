# Incluimos el paquete "math" para poder usar la función "ceil", la cual devuelve el valor
# del entero inmediato superior al número que se pasa como parámetro.
import math


class BinaryTreeList(list):
    # Nuevamente, vamos a crear una clase que hereda de la clase "list". Expresamente usaremos número para
    # simplificar el uso del árbol.

    # Constructor de la clase que inicializa la clase "list" de la que hereda.
    # Como en Stack y Queue, el constructor recibe un parámetro el cual será un árbol inicial.
    def __init__(self, tree=None):
        if tree is None:
            super().__init__(list())
        else:
            super().__init__(tree)

    def set_tree(self, tree):
        self.__init__(tree)

    def tree_size(self):
        return len(self)

    def tree_empty(self):
        return self.tree_size() == 0 if True else False

    def get_tree(self):
        return self

    def show_tree(self):
        print('Tree: %s' % str(self.get_tree()))

    def search_number(self, number: int) -> int:
        position = -1

        if not self.tree_empty():
            ini = 0
            end = self.tree_size() - 1
            offset = 0
            right = 0

            while ini <= end and offset >= 0:
                offset = math.ceil((ini + end) / 2)

                # print('Posición a comparar: %i.' % (offset + 1))
                print('¿Es %i igual a %i?' % (number, self[offset]))
                if not number == self[offset]:
                    if number > self[offset]:
                        # print('--> No, seguir buscando por la DERECHA si es que hay más números.')
                        ini = offset + 1
                        right = 1
                    else:
                        # print('--> No, seguir buscando por la IZQUIERDA, si es que hay más números.')
                        end = offset - 1
                else:
                    # print('--> Sí son iguales, fin de la búsqueda.')
                    offset = -1
                    right = 0

            position = offset + right

            if offset == -1:
                print('El número %i ya existe en el árbol (-1).' % number)
            else:
                print('El número %i ** NO ** existe en el árbol.' % number)

        return position

    def add_number(self, number: int):
        add_posotion = self.search_number(number)

        if add_posotion >= 0:
            print('Agregar %i en posición %i.' % (number, add_posotion + 1))
            self.insert(add_posotion, number)


if __name__ == '__main__':
    print('Declaración del primer arbol "my_tree"')
    my_tree = BinaryTreeList()
    my_tree.show_tree()

    print('Inicialización del árbol.')
    my_tree.set_tree(list([1, 5, 10, 30, 50, 100]))

    print('Agregar "99" al árbol.')
    my_tree.add_number(99)

    print('Buscar "200" al árbol.')
    my_tree.search_number(200)

    print('Mostrar contenido de "my_tree"')
    my_tree.show_tree()

    print('Crear segundo árbol "other_tree" inizializado con "my_tree"')
    other_tree = BinaryTreeList(my_tree)
    other_tree.show_tree()

    print('Buscar "30" en "other_tree"')
    other_tree.search_number(30)

    print('Agregar "200" al árbol.')
    other_tree.add_number(200)

    print('Agregar "150" al árbol.')
    other_tree.add_number(150)

    print('Mostrar "other_tree"')
    other_tree.show_tree()
