from Stack import Stack as stck # Importamos la clase que declaramos antes.


class ValidaParentesis:
    # Esta nueva clase recibirá una cadena con paréntesis y revisará que cada parentesis se cierre con otro.
    # Vamos a usar 2 objetos de la clase Stack para comparar los parentesis, uno para recibir la cadena y otro
    # para hacer las comparaciones según se lea la cadena de texto.
    initial_stack = stck()
    valid_stack = stck()

    # Con este método se toma carácter de la cadena de paréntesis y los mete a "initial_stack"
    def push_parentesis(self, parentesis):
        # Python permite leer strings como si fueran arreglos, así que podemos recorrer
        # "parentesis" con un ciclo.
        for char in parentesis:
            self.initial_stack.push(char)

        self.initial_stack.show_stack()

    # Este método hará push y pop entre stacks para validar la cadena que se pasó.
    # Escribí este código con algunas libertades para mostrarte que no se necesita
    # declarar variables, si no que usando métodos se puede hacer toda la lógica.
    def run_validation(self, parentesis):
        # Declaramos la variable que devolverá el resultado del método.
        valid = True

        # Usamos el método que declaramos para leer la cadena de texto.
        self.push_parentesis(parentesis)

        # Mientras "initial_stack" no esté vacío, se buscará que todos los parentsis de la cadena se cierren entre si.
        while not self.initial_stack.stack_empty():
            # Tomamos el primer elemento de la cadena que recibimos como parámetro.
            elem = self.initial_stack.pop()

            # Si el parentesis cierra, lo metemos a la pila "valid_stack" para compararlo después.
            if elem == ')':
                print('Elemento ")"')

                self.valid_stack.push(elem)
            else:
                # Como el parentesis abre, entonces checamos que haya un paréntesis que lo cierra.
                print('Elemento "("')

                # Primero checamos que el stack con los parentesis que cierran no esté vacía.
                if not self.valid_stack.stack_empty():
                    # De haber elementos, se saca uno, que es el paréntesis que cierra al elemento
                    # que sacamos de "initial_stack".
                    out = self.valid_stack.pop()
                else:
                    # Como ya no hay valores para comparar el último paréntesis que sacamos de "initial_stack" quiere
                    # decir que no hay un paréntesis que cierra y por lo tanto la cadena que recibimos es inválida.
                    valid = False

                    # Esta instrucción es para terminar el ciclo, porque no es necesario
                    # revisar el resto de los elementos de "initial_stack".
                    break

        # Antes de devolver el resultado del método, dado que ya no hay elementos en "initial_stack",
        # hay que ver que no hayan quedado elementos en "valid_stack". De haber alguno, quiere decir que quedaron
        # parentesis que abren, es decir, la cadena que se pasó es incompleta.
        if not self.valid_stack.stack_empty():
            valid = False

        # Devolvemos el resultado.
        return valid

    # Este método sólo servirá para recibir la cadena a validar y decir si es válida o no.
    def validate(self, parentesis):
        if self.run_validation(parentesis):
            print('La cadena es valida.')
        else:
            print('La cadena NO es valida')


if __name__ == '__main__':
    # Declaramos un objeto de la clase y corremos pruebas.
    valida_parentesis = ValidaParentesis()

    valida_parentesis.validate('()')
    valida_parentesis.validate('(()())')
    valida_parentesis.validate('((())')
    valida_parentesis.validate('())')
