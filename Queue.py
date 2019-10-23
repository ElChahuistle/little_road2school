class Queue:

    # A diferencia de Stack, en este ejemplo usaré algunas funciones y bondades de Python
    # para simplificar la implentación del queue y veas lo que se puede hacer con el lenguaje.
    queue = list()

    # Usando len sacamos el tamaño del queue.
    def queue_size(self):
        return len(self.queue)

    # Este método devuelte True si el queue está vacío, de lo contrario False.
    def empty(self):
        # Aquí usé un "if" que se le llama "in-line", que es una simplificación de la estructura
        # if ... else tradicional. La ventaja de este enunciado es eliminar el uso de variables.
        return self.queue_size() == 0 if True else False

    # Agrega un elemento al final de la lista. El método "insert" recibe dos parámetros: el primero es
    # el índice donde se pone el elemento y el segudo es el elemento. El índice 0 es el primer lugar en el queue.
    def queue_element(self, element):
        self.queue.insert(0, element)

    # Con este método sacamos el primer elemento del queue.
    def dequeue_element(self):
        if not self.empty():
            return self.queue.pop()

    # Devuelve el queue
    def get_queue(self):
        return self.queue

    # Muestra el queue
    def show_queue(self):
        print(str(self.queue))


if __name__ == '__main__':
    queue = Queue()

    queue.show_queue()
    queue.queue_element('lunes')
    queue.show_queue()

    print('Meter el resto de los días de la semana:')
    queue.queue_element('martes')
    queue.queue_element('miércoles')
    queue.queue_element('jueves')
    queue.queue_element('viernes')
    queue.queue_element('sábado')
    queue.queue_element('domingo')
    queue.show_queue()

    print('Sacar los días de la semana del queue.')
    # "range" es un método para hacer secuencias de números, cuando sólo se le pasa un valor se asume que
    # la secuencia comienza en 1 hasta el valor que se pasó como parámetro, en este caso, una secuencia de 1 hasta 7.
    for dia in range(7):
        print(queue.dequeue_element())

    print('Estado final del queue:')
    queue.show_queue()
