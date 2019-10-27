# El primer import ("from __future__ import annotations") permite hacer referencia a la misma clase; esto permite al
# interprete leer el código y considerar que la clase se puede usar asimisma, de lo contrario habría un error pues se
# haría referencia a una clase que no ha sido definida.
#
# También incluimos el paquete "math" para poder usar la función "ceil", la cual devuelve el valor del entero inmediato
# superior al número que se pasa como parámetro, esto porque habrá ocasiones que se obtengan números decimales al
# momento de buscar nuevas posiciones.
from __future__ import annotations
import math


class BinaryTreeList(list):
    # Nuevamente, definimos una clase que hereda de la clase "list". Expresamente usaremos número para
    # simplificar el uso del árbol.

    # Constructor de la clase que inicializa la clase "list" de la que hereda.
    # Como en Stack y Queue, el constructor recibe un parámetro el cual será un árbol inicial.
    def __init__(self, tree=None):
        if tree is not None:
            super().__init__(tree)
        else:
            super().__init__()

    # Este método asigna un árbol nuevo al objeto. La declaración del parámetro "tree: BinaryTreeList" indica que el
    # tipo de dato que se pasa como parámetro. Si el objeto no es el tipo que se pasa, entonces se devolerá un error.
    def set_tree(self, tree: BinaryTreeList):
        self.__init__(tree)

    # Devuelve el tamaño del árbol.
    def tree_size(self):
        return len(self)

    # Indica si el árbol está vacío.
    def tree_empty(self):
        return self.tree_size() == 0 if True else False

    # El árbol se devuelve asimismo. En este caso, la declaración "def get_tree(self) -> BinaryTreeList:"
    # indica al traductor que el tipo del objeto a devolver es de la clase "BinaryTreeList".
    def get_tree(self) -> BinaryTreeList:
        return self

    # Este método sólo muestra el árbol.
    def show_tree(self):
        print('Tree: %s' % str(self.get_tree()))

    # Este es el método relevante de la clase. Primero la definición muestra que se espera un entero (int) y a la vez
    # el tipo de dato que se devolverá, en este caso, un entero - Al declarar el tipo de dato a devolver, el traductor
    # espera que en la definición del método al menos un "return", que de no existir el traductor devolverá un error.

    # Este método se encargará de buscar el número que se pasa como parámetro; la búsqueda obviamente será binaria. En
    # caso de encontrar el número, devolverá un -1, de lo contrario devolverá la posición que le tocaría a ese número
    # si es que se desea agregar al árbol. Esta definición nos permite reutilizar el método y usarlo simplemente para
    # buscar un número en árbol o agregarlo si es necesario.
    def search_number(self, number: int) -> int:

        # Esta variable será la que se deolverá como el resultado de la búsqueda. Se le asigna 0 porque el árbol
        # podría estar vacío, así que sería obvio que el número no existe en el árbol y se insertaría en el índice
        # inicial, es decir, 0.
        position = 0

        # En caso de que el árbol no esté vacío se procederá a la búsqueda.
        if not self.tree_empty():
            # Aquí es donde ocurre la magia. Dado que esta implementación del árbol se hace basado en una lista,
            # la cual la estamos usando como un arreglo, declaramos los límites de la búsqueda.

            # Dado que las listas de Python usan "0" como la primera posición, la variable "ini" (que será el límite
            # inferior de la lista) se le asigna "0", porque es el límite inicial de la búsqueda. La variable "end"
            # se declara con el límite superior de la búsqueda, así que el valor inicial de la variable es el último
            # índice de la lista, el cual será el tamaño de la lista, pero como el primer índice es "0", entonces hay
            # que quitarle 1 al tamaño del árbol. Por ejemplo, si en el árbol hay 3 números, los índices de la lista
            # serán 0, 1, 2. A final de cuentas los límites iniciales del árbol son "0 a (número de elementos - 1)".
            ini = 0
            end = self.tree_size() - 1

            # El offset es una variable que nos dirá la posición en el árbol que se "visita", así que irá tomando el
            # el valor del índice de la lista que se evaluará.
            offset = 0

            # Esta variable la declaré por conveniencia y no pelarmela en la lógica de las operaciones para obtener
            # el offset de la lista. La cuestión es que para agregar valores a la lista, en vez de ir partiéndola, uso
            # el built-in "insert", el cual mete un elemento exactamente en el lugar que se le da como parámetro; por
            # ejemplo, si tengo la lista a = [1, 2, 3] y hago a.insert(1, 10) el valor se va a insertar entre 1 y 2. Lo
            # anterior está bien si quiero insertar un valor a la izquierda del 2, pero si quisiera insertar un valor
            # a su derecha tendría que hacer a.insert(2, 10).

            # Así que "right" lo único que hace es "mover" la posición un lugar a la derecha cuando necesite insertar
            # valor a la derecha (o después) de la posición actual del offset.
            # Durante la ejecución, si la búsqueda se va por la derecha, "right" será igual a 1, de lo contrario será 0.
            right = 0

            # Este ciclo se va a ejecutar mientras los límites de la búsqueda tengan un rango válido, es decir, que
            # el límite inferior "ini" sea menor o igual al límite superior "end". El usar "<=" para la comparación
            # permite que "ini" y "end" apunten al mismo índice, lo que permite considerar un sólo elemento, que en
            # este caso sería el último elemento de la lista a comparar.

            # Adicionalmente, condicionamos el ciclo a ejecutarse mientras no encuentre el número que buscamos. Dado
            # que -1 es el valor que indica que se encontró un elemento, mientras el offset no tome ese valor se
            # continuará con la búsqueda.

            # En resumén, la condición del "while" se puede leer como "recorre el árbol mientras haya elementos a
            # considerar y no se encuentre el parámetro number".
            while ini <= end and offset >= 0:

                # El siguiente elemento a considerar es determinado por la suma de los límtes entre 2 y ser redondeado
                # al entero inmediato superior en caso de que el resultado tenga decimales. Por ejemplo, en la lista
                # a = (1, 5 , 34, 98, 100) la fórmula será ( 0 + 5 ) / 2 no dará 2.5, con ceil será 3, entonces el
                # el valor a considerar en será el del índice 3, es decir, 34.

                # Según se ejecute el código bajo el "while", "offset" tomará diferentes valores, según los valores de
                # "ini" y "end".
                offset = math.ceil((ini + end) / 2)

                # Tomamos el valor del índice que "offset" indica y se checa si ese valor es igual al número que se
                # paso como parámetro.
                print('¿Es %i igual a %i?' % (number, self[offset]))
                if not number == self[offset]:

                    # En caso los valores del índice y el parámetro no sean iguales, entonces moveremos los límites
                    # para seguir búscando el valor. Los límites se moverán dependiendo si el valor que se busca es
                    # menor o mayor al número del índice contra el cual lo comparamos.
                    if number > self[offset]:

                        # Si el valor del parámetro es mayor al valor del índice, entonces seguiremos la búsqueda por
                        # la derecha del número visitado. Para ello, se mueve el límite inferior al índice que está
                        # inmediatamente a la derecha del valor visitado, con esto acotamos el número de elementos de
                        # la búsqueda, lo cual incluye descartar el índice recién comparado.
                        ini = offset + 1

                        # Como la búsqueda será por la derecha, en caso de que no se encuentre el valor, el valor de
                        # esta variable hará que el valor del parámetro number se inserte en la posición inmediatamente
                        # a la derecha del elemento visitado.
                        right = 1
                    else:

                        # Este es el caso contrario, cuando el valor del parámetro number es menor al valor del
                        # índice visitado, pero en vez de mover el límite inferior movemos el límite superior a la
                        # posición inmediatamente a la izquierda del índice visitado.
                        end = offset - 1
                        right = 0
                else:
                    # Si se encuentra el número que se pasa como parámentro, entonces se devolverá el offset = -1
                    # para indicar que no hay una posición "disponible" para acomodar el número comparado, en caso
                    # de querer insertar ese número al árbol.
                    offset = -1
                    right = 0

            # Con esta asignación indicamos si se encontró "number" con -1, de lo contrario será la posición en
            # donde se podría insertar el número.
            position = offset + right

        if position == -1:
            print('El número %i ya existe en el árbol (-1).' % number)
        else:
            print('El número %i ** NO ** existe en el árbol.' % number)

        return position

    # Este método agregará un número al árbol si es que este no existe, para lo cual usaremos el método "search_number"
    # que en caso de no encontrar el número en el árbol nos dará la posición donde se insertaría el valor del parámetro.
    def add_number(self, number: int):

        # Se le asigna a la variable la posisición donde se insertaría el parámetro, de lo contrario habrá un -1 que
        # significa que el número ya existe en el árbol.
        add_position = self.search_number(number)

        # En caso de que "add_position" no sea -1, insertar el valor en el índice que indique la variable.
        if not add_position == -1:
            print('Agregar %i en posición %i.' % (number, add_position + 1))
            self.insert(add_position, number)


if __name__ == '__main__':
    print('Declaración del primer arbol "my_tree"')
    my_tree = BinaryTreeList()
    my_tree.show_tree()

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
