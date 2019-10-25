# La clase "UnaCalculadoraMuySimple" herederá de Queue, así que internamente será un queue. Dentro de la clase
# usaremos instancias de Stack para el control de operaciones y dígitos.

# Importamos las clases que creamos antes para usarlas en la clase que vamos a declarar.
from DataStructures import Stack, Queue


class UnaCalculadoraMuySimple(Queue):
    # Esta es una implementación MUY simple de una calculadora... Y a pesar de ello, como sea quedó un código
    # medio complejo, pero espero que no sea dificil de comprender. No estoy validando la precedencia de operadores,
    # tampoco si hay parentesis. Los dígitos y operadores se evaluaran en el orden que estén en la cadena y el
    # resultado de la operación anterior se acumulará para ser utilizado en la siguiente operación.

    # Método constructor que podría recibir una expresión para inicializar el objeto.
    def __init__(self, calculation=None):
        # Inicialización de la clase Queue con la cadena que se pase como parámetro.
        
        # Tal como pasa con la declaración de Queue (donde inicializamos la clase "list" de la que se hereda)
        # hacemos lo mismo en esta clase al inicializar Queue.
        Queue.__init__(self, calculation)

        # Declaración de stacks para llevar control de las operaciones y dígitos.
        self.opers = Stack()
        self.numbers = Stack()

    # Método para pasar una expresión al objeto.
    def set_calculation(self, calculation):
        self.__init__(calculation)

    # Muestra la cadena que se pasó para evaluar.
    def show_calculation(self):
        self.show_queue()

    # Evaluar y resolver expresión.
    def sort_calculation(self):
        rslt = None  # Con esta variable se devolverá el mensaje de error, en caso de haber alguno.
        calculation = 0  # Variable con la que se "acumulará" el resultado de las operaciones.

        # Primero revisar que se haya pasado alguna cadena para evaluarse.
        if not self.queue_empty():
            numero = ''

            # Dado que la cadena no está vacía, vamos a leerla mientras haya valores.
            while not self.queue_empty():
                # Obtenemos el siguiente elemento de la cadena.
                element = self.dequeue()

                # Si el elemento es un espacio, entonces ignorarlo.
                if not element == ' ':

                    # Si es una operación, meterla al stack de operaciones.
                    if element in ('+', '-', '*', '/'):

                        # Cuando se encuentra una operación quiere decir que no hay más números a concatenar, así que
                        # el número completo se mete al stack de números, luego se reinicia la variable.
                        if not numero == '':
                            self.numbers.push(float(numero))
                            numero = ''
                        else:
                            # En caso de haber una operación, pero no un número, entonces la expresión es inválida.
                            break

                        self.opers.push(element)
                    elif element.isdigit() or (element == '.' and not numero == ''):

                        # Dado que la expresión se evalua elemento por elemento, se obtendrá dígito por dígito,
                        # entonces según aparezcan se irán concatenado para formar el número completo. En caso de que
                        # el número tenga decimales, concatenar el punto al número completo.
                        numero = element + numero
                    else:

                        # En caso de que haya un elemento que no sea una operación o dígito, devolver error.
                        rslt = 'La cadena del cálculo es inválida.'
                        break  # Este comando es para terminar (o salir) el ciclo.

            if not numero == '':
                print('Número completo: %s.' % numero)
                self.numbers.push(float(numero))

            # Si no hay un mensaje de error, hay operandores que procesar y al menos 2 digitos,
            # se procede a evaluar la expresión.
            if rslt is None and not (self.opers.stack_empty() or self.numbers.stack_size() < 2):
                # Tomamos el primer valor a evaluar. Esto podría interprestarse como el primer
                # resultado de evaluar la expresión.
                calculation = self.numbers.pop()

                # Ciclarse mientras haya dígitos en el stack de dígitos.
                while not self.numbers.stack_empty():

                    # Proceder sólo si hay operaciones disponible.
                    if not self.opers.stack_empty():
                        # Sacar la siguiente operación disponible.
                        oper = self.opers.pop()

                        # Validar que haya otro dígito a considerar.
                        if not self.numbers.stack_empty():
                            # Tomar el siguiente dígito a evaluar.
                            digit = self.numbers.pop()

                            # Este es un mensaje de seguimiento para ver qué sucede durante la evaluación
                            # de la expresión.
                            print('Operación: %f %s %f' % (calculation, oper, digit))

                            # Ejecutar operación con el valor acumulado y el último dígito obtenido.
                            # El resultado de la operación se acumula en la variable "calculation".
                            if oper == '+':
                                calculation += digit
                            elif oper == '-':
                                calculation -= digit
                            elif oper == '*':
                                calculation *= digit
                            elif oper == '/':

                                # Esto es para evitar una excepción por dividir entre 0.
                                if not digit == 0:
                                    calculation /= digit
                                else:
                                    # En caso de que el dígito sea un cero, el valor acumulado al momento será cero.
                                    calculation = 0
                        else:
                            # Si falta un dígito para continuar con la evaluación de la expresión, devolver error.
                            rslt = 'Falta al menos un dígito para la operación %s.' % oper
                            break  # Este comando es para terminar el ciclo.
                    else:
                        # En caso que falté algún operador para seguir evaluando la expresión, devolver error.
                        rslt = 'Falta operando.'
                        break  # Este comando es para terminar el ciclo.
            else:
                # En caso de que haya un error previo, no haya operaciones o al menos 2 dígitos, devolver error.
                rslt = 'La cadena del cálculo es inválida.'
        else:
            # En caso de que no haya una expresión a evaluar, devolver error.
            rslt = 'No hay una expresión a procesar.'

        # Si no hubo algún error durante la evaluación de la expresión, mostrar el resultado...
        if rslt is None:
            print('El resultado del cálculo es: %s.' % str(calculation))
        else:  # ... De lo contrario mostrar el mensaje de error.
            print(rslt)


if __name__ == '__main__':
    cal = UnaCalculadoraMuySimple()

    # Esto devolverá un error porque no hay expresión a evaluarse.
    cal.sort_calculation()

    # Esta cadena devolverá 3. Notar que hay un espacio, el cual será ignorado.
    cal.set_calculation('2 +1')
    cal.sort_calculation()

    # Esta cadena devolverá 15. Notar los espacios, los cuales serán ignorados.
    cal.set_calculation('3* 5 ')
    cal.sort_calculation()
