from __future__ import annotations
from DataStructures import Stack


class BinaryTreeTuple:

    # Sólo para tenerlo en cuenta, un binary tree está compuesto de una raíz (root), ramas (branches) y hojas (leafs);
    # otra manera de llamarle a las hojas es nodos (nodes). He aquí algunas observaciones sobre binary trees:
    #   1. La profundidad de un árbol se refiere a todos los niveles que tiene el árbol.
    #   2. La cardinalidad de un árbol es el número de nodos que este tiene.
    #   3. Un nodo podría no tener hijos y a lo mucho 2.
    #   4. Un nodo siempre tiene un padre (y sólo uno), excepto root.
    #   5. El descenso en árbol se hace a través de las ramas del mismo.
    #   6. Evaluar un nodo, después de ser encontrado durante el descenso, también se le dice "visitar".
    #
    # En esta implementación de binary tree usaremos la estrategia "bottom to top", lo que quiere decir que para obtener
    # la respuesta partimos de lo general y procesamos hasta llegar a lo particular; una vez que llegamos al caso
    # particular se construye la respuesta a partir de ese caso hasta regresar a lo general. En el caso de un binary
    # tree usualmente se dice que bajamos hasta lo más profundo de un árbol (lo cual se hace a través de sus ramas) y
    # encontrado o no lo que se busca, se construye hacía arriba la respuesta.
    #
    # Esta implementación del árbol binario usará el tipo de dato "tuple" como la hoja o nodo. El constructor
    # inicializa la raíz del árbol ("root") a None porque al momento no hay nodos en el árbol. Por conveniencia,
    # también habrá un stack que nos servirá para buscar números en el árbol, el cual servirá para llevar memoria
    # de los nodos visitados durante la búsqueda; este stack nos servirá para agregar un nuevo nodo al árbol, en caso
    # de ser necesario.

    def __init__(self):
        self.root = None
        self.stack = Stack()

    # Método "clásico" para saber si hay elementos en el árbol.
    def tree_empty(self):
        return self.root is None if True else False

    # Método para buscar un número en el árbol. Recibe un número como parámetro. Si encuentra el número devolverá
    # True, de lo contrario False.
    def number_in_tree(self, number: int) -> bool:
        # El resultado por default del método. En caso de que el número se encuentre, tomará el valor True.
        number_found = False

        # Para buscar el número, creamos un árbol temporal, que será igual al árbol existente.
        search_root = self.root

        # Con esta declaración reseteamos el stack de los resultados de la búsqueda.
        self.stack = None

        print('Buscar número "%i" en árbol.' % number)

        # Mientras el árbol de búsqueda no esté vacío o no se haya encontrado el número, la búsqueda continuará.
        # La condición del while se podría también escribir así: search_root is not None and not number_found. ¿Por qué
        # la escribí diferente? En este caso "not" es un factor común de ambas evaluaciones, así que lo podemos sacar
        # para afectar ambas variables, en otras palabras, negar toda la expresión, en vez de hacerlo individualmente;
        # ahora, como estamos negando toda la expresión, el "and" debe cambiar a "or", es decir, la operación contraria.
        while not (search_root is None or number_found):

            # El tipo de dato tuple por si mismo puede descomponerse en sus partes, sin necesidad de hacer nada más.
            # En este caso, cada elemento del árbol es una tupla compuesta de 3 valores: el número, una rama
            # izquierda y una rama por la derecha. Python descompone (o explota) la tupla y asigna cada valor
            # a las variables de la asignación, lo cual hace muy conveniente. En este caso la tupla tiene 3 valores (en
            # este orden): nùmero, rama izquierda y rama derecha.
            tuple_num, left, right = search_root

            # Validar si el número que se busca es igual el que se obtuvo de la tupla.
            if not number == tuple_num:

                # Si el número no es igual al de la tupla, etonces guardamos la tupla para usarla después, si es que
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

                # En caso de que el número se encuentre, entonces se devolverá True.
                print('El número %i ya existe en árbol.' % number)
                number_found = True

        # Devolver el resultado de la búsqueda.
        return number_found

    # Este método agregará al árbol el número que se pasa como parámetro, si es que este no existe ya en el árbol.
    def add_number(self, number: int):

        # Si el número no existe en el árbol, entonces agregarlo al árbol.
        if not self.number_in_tree(number):
            print('Add Number "%i".' % number)

            # Se crea una tupla para el número que se pasó como parámetro.
            new_tree = tuple([number, None, None])

            # El método "number_in_tree" crea lo que llamaremos el stack de la respuesta. Con ese stack podemos
            # construir el árbol que incluye el número que obtuvimos como parámentro.
            while not self.stack.stack_empty():

                # Se obtine la tupla y se descompone en sus valores atómicos, es decir, el número, rama izquierda y
                # rama derecha.
                node_value, node_left, node_right = self.stack.pop()

                # Si el número que se pasó como parámetro es mayor al valor de la tupla, entonces la nueva tupla
                # se asigna como la rama derecha de la tupla que se obtuvo del stack, de lo contrario se asignará
                # a la rama izquierda.
                if number > node_value:
                    node_right = new_tree
                else:
                    node_left = new_tree

                # Ahora el árbol nuevo será igual a la rama recién creada.
                new_tree = tuple([node_value, node_left, node_right])

            # Finalmente, una vez reconstruido el árbol con el número que recibimos, se asigna a la ráiz del árbol.
            self.root = new_tree

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


class BinaryTreeNode:
    def __init__(self):
        self.root = None
        self.stack = Stack()

    def is_num_tree(self, number: int) -> bool:
        # El valor default de la respuesta; dado que una posibilidad es que árbol esté vacío, entonces inmediatamente
        # brincará al return del método.
        node_found = False

        # Primero validar que haya valores en el árbol.
        if self.root is not None:
            # Si no hay valores en el árbol obtenemos la raíz del árbol; recordar que esta raíz podría tener más nodos
            # abajo de ella.
            root = self.root

            # Con esta declaración reseteamos el stack de búsqueda.
            self.stack = None

            while not (root is None or node_found):
                if not number == root.get_value():

                    self.stack.push(root)
                    if number > root.get_value():
                        root = root.get_right_node()
                    else:
                        root = root.get_left_node()
                else:
                    node_found = True

        return node_found

    def add_number(self, number: int):
        if not self.is_num_tree(number):

            new_tree = Node(number)
            while not self.stack.stack_empty():
                stack_node = self.stack.pop()

                if new_tree.get_value() > stack_node.get_value():
                    stack_node.set_right(new_tree)
                else:
                    stack_node.set_left(new_tree)

                new_tree = stack_node

            self.root = new_tree
