from __future__ import annotations


class Stack(list):
    # En esta ocasión usaremos herencia para definir la clase Stack. Además la implementación
    # será usando los "built-in" que ofrecen las clases standard de Python.
    # La herencia en Python se define pasando como parámetro la clase de la que se hereda a la clase
    # que estamos definiendo.

    # Dado que Stack hereda de list, no es necesaraio declarar otro objeto, al contrario,
    # la clase por si misma es el objeto que usamos en la primera implementación de Stack.

    # El método "__init__" es el método constructor de la clase "Stack", es decir, es el método
    # que inicializa la clase, se podría decir que en otras palabras construye al objeto/instancia de la clase.
    # Todas las clases inerentemente tienen un método constructor. En el caso de Python siempre hay un método
    # "__init__" por default, por eso no es necesario declararlo siempre.
    def __init__(self, elements=None):
        # En este caso lo que quiero es que al declarar un objeto de esta clase pueda inicializarlo con algún valor.
        # Dado que estoy declarando el método constructor de "Stack" y estamos heredando de "list", entonces (en Python)
        # necesito inizializar "list" también (yo sé, es medio confuso), eso lo hago con el método "super()", que
        # es un método que llama a la clase de la que heredamos y aunque podría invocar cualquier método de la clase,
        # en este momento sólo me interesa inizializarla con el valor que recibí en el parámetro "elements".

        # Esta condición es para pasar una cadena vacía en caso de que no se pase algún parámetro al constructor.
        if elements is None:
            # Si no se pasa algún valor ("None") entonces el stack se inicializa con una lista vacía.
            super().__init__(list())
        else:
            # Si se recibe un parámetro entoncces con él se inicializa el stack.
            super().__init__(elements)

    # Este método servirá para asignar un valor (por ejemplo, un string) al stack. El uso de este método es para
    # asignar un valor a la clase después de haber sido declarada. Esto es últil cuando declaramos el objeto sin
    # valor inicial o cuando sea necesario cambiar el contenido del stack.
    # Ahora, dado que este método haría lo mismo que el constructor, sólo es necesario llamar el constructor de
    # la clase para asignar el valor del stack como si lo declararamos por primera vez. A esto se le llama
    # "reutilización de código".
    def set_stack(self, elements):
        self.__init__(elements)

    # Asimismo, en ves de concatenar a la lista un elemento, usamos el built-in "append" para
    # meter el elemento al stack.
    def push(self, element):
        self.append(element)

    # Podríamos declarar un método "pop", pero carece de sentido porque nuestra clase "Stack"
    # hereda de la clase "List", la cual ya tiene un método propietario "pop".

    # Incluimos los métodos de "size" y "empty" para fines de manejo del stack.
    def stack_size(self):
        return len(self)

    def stack_empty(self):
        return self.stack_size() == 0 if True else False

    # Este método es para obtener el mismo stack. Este método es para fines
    # prácticos en posteriores implementaciones de la clase.
    def return_stack(self) -> Stack:
        return self

    # Agregamos el método para mostrar el "Stack".
    def show_stack(self):
        print('Stack: %s' % (str(self.return_stack())))


class Queue(list):
    # Las explicaciones que pudiera dar sobre la declaración de esta clase son las mismas que para "Stack",
    # aunque el uso de los métodos propietarios de "list" se usan con otra filosofía que, en vez de "último que
    # entra es el primero que sale" (Last In - First Out, LIFO), será la filosofía "el primero que entra, es el
    # primero que sale" (First In - First out, FIFO).
    def __init__(self, elements=None):
        if elements is None:
            super().__init__(list())
        else:
            super().__init__(elements)

    def set_queue(self, elements):
        self.__init__(elements)

    def queue(self, element):
        self.insert(0, element)

    def dequeue(self):
        return self.pop()

    def queue_size(self):
        return len(self)

    def queue_empty(self):
        return self.queue_size() == 0 if True else False

    def return_queue(self) -> Queue:
        return self

    def show_queue(self):
        print('Queue: %s' % str(self.return_queue()))
