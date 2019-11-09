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
    def __init__(self, number: int = None):
        self.number = number
        self.left = None
        self.right = None

    def set_value(self, number: int):
        self.__init__(number)

    def get_value(self) -> int:
        return self.number

    def set_left_node(self, node: Node) -> Node:
        self.left = node
        return self

    def set_right_node(self, node: Node) -> Node:
        self.right = node
        return self

    def get_left_node(self) -> Node:
        return self.left

    def get_right_node(self) -> Node:
        return self.right

    def empty_right_node(self) -> bool:
        return self.right is None if True else False

    def empty_left_node(self) -> bool:
        return self.left is None if True else False


class BinaryTreeNode:
    # En función esta clase funciona igual que "BinaryTreeTuple", con la diferencia que usamos el objeto Node en vez
    # de tuple para almacenar el número y las ramas que salen de cada nodo. De ahí que no hondaré en explicaciones
    # porque los métodos hacen exactamente lo mismo que en "BinaryTreeTuple".
    def __init__(self):
        self.root = None
        self.stack = Stack()

    # Este método busca un número en el binary tree. Durante la búsqueda guardará los nodos que visita en caso de
    # este número se vaya a agregar al árbol.
    def is_num_tree(self, number: int) -> bool:
        # El valor default de la respuesta; dado que una posibilidad es que árbol esté vacío, entonces inmediatamente
        # brincará al return del método.
        node_found = False

        # Primero validar que haya nodos en el árbol.
        if self.root is not None:
            # Si no hay nodos en el árbol obtenemos la raíz del árbol; recordar que esta raíz podría tener más nodos
            # abajo de ella.
            root = self.root

            # Con esta declaración reseteamos el stack de búsqueda.
            self.stack = Stack()

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

    # Tal como lo hicimos en la clase "BinaryTreeTuple" este método agregará el número al binary tree.
    def add_number(self, number: int):
        # Buscamos el número en el árbol para saber si existe. Tal como en "BinaryTreeTuple" el stack que se genere
        # durante la búsqueda nos servirá para armar el nuevo árbol con el número que entra como parámetro.
        if not self.is_num_tree(number):

            # De entrada este nodo será el que tenga el valor que queremos agregar al árbol, pero reutilizaremos
            # este objeto para construir el árbol que incluya el nodo nuevo.
            new_tree = Node(number)

            # Ahora vamos a traer los nodos que se guardaron durante la búsqueda para hacerlos parte del nuevo
            # árbol que incluye el nodo nuevo.
            while not self.stack.stack_empty():
                stack_node = self.stack.pop()

                # Vemos en qué rama debe ir el árbol con la respuesta.
                if new_tree.get_value() > stack_node.get_value():
                    stack_node.set_right_node(new_tree)
                else:
                    stack_node.set_left_node(new_tree)

                # Asignamos el árbol recién armado al nodo que trae el resultado de agregar el nuevo nodo.
                new_tree = stack_node

            # Una vez que todos los nodos han sido considerados, el árbol final que quedó en "new_tree" es el árbol
            # anterior, pero incluyendo el nodo nuevo, así que "new_tree" se convierte en root.
            self.root = new_tree


class BinaryTreeRecursive:
    # Esta implementación de árbol binario usa recursividad para buscar y agregar números de ser necesario. En
    # comparación con las dos implementaciones anteriores es que se usa menos código, sólo que el código es un poco
    # difícil de entender.

    # El constructor es similar a los de las otras implementaciones, sólo que ya no necesitamos el stack, de hecho,
    # el uso de un stack sirvió para simular recursividad, de ahí que ya no lo estemos usando.
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    # Este método es recursivo, se llama asimismo para hacer la búsqueda. Pasamos un nodo como parámetro como el "punto
    # de partida". La idea es que lidiamos con un nodo a la vez. El caso más elemental es que sólo haya un nodo, uno
    # que no tenga hijos. Así que cuando cuando se tenga un sólo nodo, comparamos el valor del nodo con el que se
    # recibió como parámetro.
    #
    # Si hay más nodos en el árbol "bajaremos" para seguir buscando el número, si es que existe.
    def search_number_bis(self, root: Node, number: int):
        # Validamos si hay un nodo a revisar.
        if root is not None:
            # Si se recibe un nodo, entonces averiguamos si su valor es el número que buscamos.
            if number == root.get_value():
                # Si el número del nodo es igual al número que recibimos como parámetro entonces devolvemos True.
                return True
            elif number < root.get_value():
                # En caso de que el valor del nodo no sea el número que buscamos, entonces seguir buscando el número
                # por las ramas. Buscaremos por la izquierda si el número que se recibió como parámetro es menor al
                # número del que estamos visitando, de lo contrario nos iremos por la rama derecha.

                # Este "return" devolverá la solución, que al final será True o False, dependiendo si encuentra un nodo
                # con el número que buscamos por la rama izquierda del árbol que recorremos.
                return self.search_number_bis(root.get_left_node(), number)
            else:
                # Este "return" es lo mismo que el anterior, sólo que la búsqueda va por la rama derecha del árbol.
                return self.search_number_bis(root.get_right_node(), number)
        else:
            # Si ya no hay nodo a revisar, entonces se devuelve False.
            return False

    # Este método contiene al método "search_tree_bi". La idea de este método es simplificar el llamado de la búsqueda
    # con el número y el nodo raíz ("self.root") como el punto de un inicio de la búsqueda.
    def search_number(self, number: int):
        # Se muestra un mensaje diferente dependiendo si se encuentra el número o no.
        if self.search_number_bis(self.get_root(), number):
            print('El número %i existe en el árbol.' % number)
        else:
            print('El número %i ** NO ** existe en el árbol.' % number)

    # Este método, si no hay más nodos que recorrer, entonces se crea un nuevo nodo con el número que se pasó como
    # parámetro. Cuando se recibe un None en vez de un nodo (Node) quiere decir que no hay más nodos que visitar, de
    # ahí que se devuelve un nodo nuevo con el valor del número que se pasó como parámetro.
    def add_number_bis(self, root: Node, number: int):
        # Esta condición valora si no se recibió algún nodo, de ser así, entonces se devuelve un nodo nuevo con el valor
        # que se pasó como parámetro, el cual se agregará a la rama que se recorrió para encontrar el lugar que le toca
        # en el árbol.
        if root is None:
            return Node(number)
        elif root.get_value() < number:
            # Si no es None quiere decir que hay más nodos que visitar en el árbol. Así que se compara el número del
            # nodo que visitamos con el que se recibió como parámetro. Si es el número del parámetro es menor al valor
            # del nodo, si es así entonces se prosigue el recorrido por la rama izquierda...
            return self.add_number_bis(root.get_left_node(), number)
        else:
            # ... Si el valor es mayor entonces se recorre la rama derecha.
            return self.add_number_bis(root.get_right_node(), number)

    # Este método es para agregar un número al árbol, si es que este no existe. Tal como "search_tree", este método
    # es sólo para pasar como punto de partida "self.root".
    def add_number(self, number: int):
        # Si no encuentra el número, se agrega un nodo con el número que se pasó como parámetro, de lo contrario, el
        # número ya existe y no hay necesidad de agregarlo al árbol.
        if not self.search_number_bis(self.get_root(), number):
            # Si no se encuentra el número en el árbol, entonces se procede a agregarlo al árbol.
            self.root = self.add_number_bis(self.get_root(), number)

            # Mostrar mensaje confirmando que el número se agregó al árbol.
            print('El número %i se agregó al árbol.' % number)
        else:
            # Si ya existe en el árbol, se muestra mensaje de que ya existe.
            print('El número %i ya existe en el árbol.' % number)


class BinaryTreeRecursiveRedux:
    def __init__(self):
        self.root = None

    def get_root(self) -> Node:
        return self.root

    # Este método es una copia del método de la clase BinaryTreeRecursive. Lo agrego para que la
    # clase esté completa con búsqueda y agregar número. Le hice unos cambios para aprovechar las
    # facilidades de Python.
    def search_number_bis(self, root: Node, number: int) -> bool:
        # No es necesario preguntar si es None, Python valora el parámetro y si es None entonces
        # devuelve False, de lo contario True. Nego el resultado para comenzar con el caso más
        # elemental, es decir, que el nodo sea y por lo tanto el número no existe en el árbol.
        if not root:
            return False

        # En caso de que el nodo (root) no sea None, procedemos a valorar si el número del nodo
        # actual es el número que buscamos. Si es así, entonces devolvemos True, porque encontramos
        # el número en el árbol.
        elif number == root.get_value():
            return True

        # Las siguientes llamadas son recursivas, es decir, el método se llama asimismo con otros parámetros
        # asumiendo que en alguna llamada posterior se encontrará la respuesta.

        # En caso de que el valor del nodo que visitamos no es igual al número del parámetro continuamos
        # la búsqueda. En caso de que el número del parámetro sea menor al valor del nodo que visitamos
        # entonces continuaremos la búsqueda por la rama izquierda del nodo actual.
        elif number < root.get_value():
            return self.search_number_bis(root.get_left_node(), number)

        # Finalmente, si el valor no es menor, entonces es mayor y por lo tanto la búsqueda continua por
        # la derecha del nodo que estamos visitando.
        else:
            return self.search_number_bis(root.get_right_node(), number)

    # Este método nos sirve para llamar el método anterior con la raíz del árbol como parámetro.
    def search_number(self, number):
        if not self.search_number_bis(self.get_root(), number):
            print('El número ** NO ** existe en el árbol!')
        else:
            print('El número existe en el árbol.')

    # Este método es recursivo y es una re-implementación del método que "add_number_bis" de la
    # clase BinaryTreeRecursive. Ahora, en vez de ejecutar la búsqueda binaria antes de intentar
    # agregar el número, el método hace ambas cosas: busca el número y lo agrega de no encontrarlo.
    def add_number_bis(self, root: Node, number: int) -> Node:

        # Esta condición checa si root es un nodo. Si es None entonces es False, es decir, no es
        # un nodo si no una rama vacía; de lo contrario quiere decir que root sí es un nodo, de ahí
        # que que devolverá True. Nego el resultado de la condición para que comience con el caso
        # más simple, es decir, que el árbol está vacío y por lo tanto se le agrega un nuevo nodo
        # con el número que recibimos como parámetro.
        if not root:

            # Mensaje de feedback para saber que el número se agregó al árbol.
            print('El número se agregó al árbol.')
            return Node(number)

        # Obtenemos el valor del nodo root y lo comparamos con el número que nos dieron
        # como parámetro. Si es verdadero significa que el número ya existe en el árbol,
        # entonces devuelve root nuevamente, dado que no hay nada más que hacer.
        elif number == root.get_value():

            # Un mensaje de feedback para saber que el número no se agregó al árbol.
            print('El número ya existe en el árbol!')
            return root

        # En caso de que el valor del nodo que se visita no sea igual procedemos a visitiar
        # el resto del árbol. Si el parámetro es menor al valor del nodo que estamos revisando
        # entonces seguimos el recorrido por la izquierda.
        elif number < root.get_value():

            # Las siguientes llamadas son recursivas, lo que quiere decir que el método se llama
            # asimismo con diferentes valores. El usar return para cada llamada es por el método
            # devuelve un nodo, entonces, para construir la respuesta (que en este caso es desde
            # lo más bajo del árbol a lo más alto) necesitamos "colocar" los nodos en el lugar
            # que les corresponde.

            # Entonces, como es recursivo, el método se llama asimismo, pero se pasa como
            # parámentro su rama izquierda y el número que estamos buscando agregar. El resultado
            # de la llamada recursiva se asignará a la rama izquierda del nodo que se visita.
            return root.set_left_node(self.add_number_bis(root.get_left_node(), number))
        else:

            # En caso de que el número sea mayor al valor del nodo que estamos visitando, entonces
            # el método se llama asimismo con la rama derecha y el mismo número como parámetro.
            # El resultado de la llamada recursiva se asignará a la rama derecha del nodo actual.
            return root.set_right_node(self.add_number_bis(root.get_right_node(), number))

    # Este método es para poder llamar al método recursivo con el nodo raíz de la clase.
    def add_number(self, number: int):
        self.add_number_bis(self.get_root(), number)


class BinaryTreeBalanced:
    def __init__(self):
        self.tree = BinaryTreeRecursive()
        self.height = 0

    def get_height_bis(self, root: Node):
        if root is None:
            return 0
        else:
            left_height = self.get_height_bis(root.get_left_node())
            right_height = self.get_height_bis(root.get_right_node())

            return left_height < right_height if right_height else left_height

    def get_height(self):
        self.height = self.get_height_bis(self.tree.get_root())

    def add_number(self, number: int):
        self.tree.add_number(number)
        self.get_height()
