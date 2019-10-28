from __future__ import annotations
from DataStructures import Stack


class BinaryTreeTuple:
    # Esta implementación del árbol binario usará el tipo de dato "tuple" para crear el árbol.

    # El constructor de la clase inicializa la raíz del árbol ("root") a None porque al momento no hay elementos en el
    # árbol. Por conveniencia, también habrá un stack que nos servirá para buscar números en el árbol, el cual se
    # puede ver como una especie de "memoria" de ejecución.
    def __init__(self):
        self.root = None
        self.stack = None

    # Método "clásico" para saber si hay elementos en el árbol.
    def tree_empty(self):
        return self.root is None if True else False

    # Método para buscar un número en el árbol. Recibe un número como parámetro. Si encuentra el número devolverá
    # True, de lo contrario False.
    def number_in_tree(self, number: int = None) -> bool:
        # El resultado por default del método. En caso de que el número se encuentre, tomará el valor True.
        number_found = False

        # Validar que se recibió un número para buscar.
        if number is not None:
            # Para buscar el número, creamos un árbol temporal, que será igual al árbol existente.
            search_root = self.root

            # Con esta declaración reseteamos el stack de los resultados de la búsqueda.
            self.stack = Stack()

            print('Search for number "%i".' % number)

            # Mientras el árbol de búsqueda no esté vacío o no se haya encontrado el número, la búsqueda continuará.
            while not (search_root is None or number_found):

                # El tipo de dato tuple por si mismo puede descomponerse en sus partes, sin necesidad de hacer nada más.
                # En este caso, cada elemento del árbol es una tupla compuesta de 3 valores: el número, una rama
                # izquierda y una rama por la derecha. Esos bvalores se obtienen y asignan a tuple_num, left y right,
                # respectivamente.
                tuple_num, left, right = search_root

                # Validar si el número que se busca es el que se obtuvo de la tupla.
                if not number == tuple_num:

                    # Si el número no existe en la tupla, etonces guardamos la tupla para usarla después, si es que
                    # agregaremos el número al árbol.
                    self.stack.push(search_root)

                    # Si el número que se busca es mayor al que se obtuvo de la tupla, entonces la búsqueda del
                    # número continuará por la rama derecha, de lo contrario la búsqueda se irá por la izquierda.
                    if number > tuple_num:

                        # El árbol de búsqueda será igual a la rama derecha de la tupla que validamos.
                        search_root = right
                    else:

                        # De lo contario, el árbol de búsqueda será igual a la rama de la deracha de la tupla.
                        search_root = left
                else:

                    # En caso de que el número se encuentre, entonces devolver True.
                    print('El número %i ya existe en árbol.' % number)
                    number_found = True

        # Devolver el resultado de la búsqueda.
        return number_found

    # Este método agregará al árbol el número que se pasa como parámetro, si es que este no existe ya en el árbol.
    def add_number(self, number: int = None):
        # Con esta declaración reseteamos el stack de búsqueda.
        self.stack = None

        # Si se pasó un número como parámetro y número no existe en el árbol, entonces agregarlo al árbol.
        if not (number is None or self.number_in_tree(number)):
            print('Add Number "%i".' % number)

            # Si el número que se pasó no existe, crear una tupla para agregarla al árbol.
            new_root = tuple([number, None, None])

            # El método "number_in_tree" crea lo que llamaremos el stack de los resultados de búsqueda. Con ese stack
            # podemos construir el árbol con el número que pasó como parámetro.
            while not self.stack.stack_empty():

                # Se obtine la tupla y se descompone en sus valores atómicos, es decir, el número, rama izquierda y
                # rama derecha.
                node_value, node_left, node_right = self.stack.pop()

                # Si el número que se pasó como parámetro es mayor al valor de la tupla, entonces la nueva tupla
                # se asigna como la rama derecha de la tupla que se obtuvo del stack, de lo contrario se asignará
                # a la rama izquierda.
                if number > node_value:
                    node_right = new_root
                else:
                    node_left = new_root

                # Ahora el árbol nuevo será igual a la rama recién creada.
                new_root = tuple([node_value, node_left, node_right])

            # Finalmente, una vez reconstruido el árbol con la respuesta, se asigna a la ráiz del árbol.
            self.root = new_root

            # Mostrar el árbol final.
            print('Árbol: %s' % str(self.root))


class Node:
    def __init__(self, number: int):
        self.number = number
        self.left = None
        self.right = None

    def get_value(self) -> int:
        return self.number

    def set_left(self, node: Node):
        self.left = node

    def set_right(self, node: Node):
        self.right = node

    def get_left(self) -> Node:
        return self.left

    def get_right(self) -> Node:
        return self.right

    def empty_right_node(self) -> bool:
        return self.right is None if True else False

    def empty_left_node(self) -> bool:
        return self.left is None if True else False


if __name__ == '__main__':
    pass
