# Definicion de clase Stack.


class Stack:
    # En Python, las variables no necesitan ser declaradas con tipos de datos. Además, los métodos de una clase
    # reciben por default el parámetro "self", más los parámetros que se definan.

    # Las variables "stack" y "elements", en el contexto de la clase se les conoce como "atributos". Usualmente
    # los atributos de una clase no deben ser accesados directamente, si no a través de "métodos".

    # En Python no existen arreglos, así que usaremos su tipo de dato list para el stack, que es como un arreglo.
    stack = []

    # Este atributo llevará la cuenta de los elementos que existen en el stack. Empieza en cero porque (d-oh!)
    # no hay elementos en el stack.
    elements = 0

    # Por lo regular los atributos de una clase sólo pueden accederse a través de métodos de la clase.
    # El método "stack_size" nos dará el valor del atributo "elements" para saber cuántos elementos hay en el stack.
    def stack_size(self):
        return self.elements

    # Por practicidad es mejor usar método que devuelva True o False, el cual se puede usar directamente en dondiciones.
    # El método "stack_empty" devuelve True cuando "stack_size" devuelve cero, de lo contrario devolvera False.
    def stack_empty(self):
        # Esta variable será la que deolveremos como el resultado del método.
        # La variable "empty" la inicializamos en False para sólo comprobar si hay elementos en el stack.
        # Se podría decir que por default el método devuelve False.
        empty = False

        # Como el default es False (que implica que el stack NO está vacía) sólo nos falta
        # comprobar que no haya elementos, es decir, que "stack_size" devuelva cero.
        if self.stack_size() == 0:
            # Si no hay elementos, entonces cambiamos el valor default por True.
            empty = True

        # Devolver el valor que haya quedado en la variable "empty".
        return empty

    # Con este método meteremos los elementos al stack. Vamos a hacerlo explícitamente en vez de
    # usar los métodos standard del tipo list.
    # Este método recibe el parámetro "value", el cual se meterá al final del atributo "stack".
    def push(self, value):
        # El parámetro se agrega al final de "stack".
        self.stack = self.stack + [value]
        # También aumentamos en uno el número de elementos en el stack.
        self.elements = self.elements + 1

    # Con este método sacaremos los elementos de "stack".
    def pop(self):
        # Esta variable la inicializamos con una lista vacía, en caso de que ya no haya elementos en el "stack".
        # Este es el valor por default, que se devolverá en caso de que "stack" esté vacío.
        element = []

        # Usando el método que devuelve True o False, preguntamos si "stack" está vacío.
        if not self.stack_empty():
            # Como no está vacío, al menos debe haber un elemento en "stack".
            # Restamos uno al número de elementos.
            self.elements = self.elements - 1
            # Tomamos el último elemento de "stack" y lo asignamos a la variable "element".
            element = self.stack[self.elements]
            # Quitamos un elemento de "stack".
            self.stack = self.stack[:self.elements]

        # Devolvemos la variable que tiene el resultado del método.
        return element

    # Usando una ventaja de Python, convertimos la lista en un string y la devolveremos.
    def get_stack(self):
        return str(self.stack)

    # Con "get_stack" obtenemos un string que ahora podemos escribir en la salida.
    def show_stack(self):
        print(self.get_stack())


if __name__ == '__main__':
    # Haremos una pequeña demostración de la clase que acabemos de declarar.
    # Declaramos un objeto de la clase Stack.
    my_stack = Stack()

    # Ahora jugamos un poco con el objeto.
    # Ejecuta el código para que veas el comportamiento.
    print('Elementos iniciales del stack: ' + my_stack.get_stack())
    print('Push elemento "A"')
    my_stack.push('A')
    print('Stack --> ' + my_stack.get_stack())
    print('Push elements "T" y "W"')
    my_stack.push('T')
    my_stack.push('W')
    print('Stack --> ' + my_stack.get_stack())
    print('Pop elemento')
    elemento = my_stack.pop()
    print('Elemento que salió del stack: "' + elemento + '"')
    print('Stack --> ' + my_stack.get_stack())
    print('Agregar elements "D", "F" y "X"')
    my_stack.push('D')
    my_stack.push('F')
    my_stack.push('X')
    print('Stack --> ' + my_stack.get_stack())
    print('Pop elemento')
    elemento = my_stack.pop()
    print('Elemento que salió del stack: "' + elemento + '"')
    print('Pop elemento')
    elemento = my_stack.pop()
    print('Elemento que salió del stack: "' + elemento + '"')
    print('Stack --> ' + my_stack.get_stack())
