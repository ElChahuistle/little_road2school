from DataStructures import Stack, Queue


class UnaCalculadoraMuySimple(Queue):
    # Esta es una implementación MUY simple de una calculadora. No estoy validando la precedencia de operadores,
    # tampoco si hay parentesis o no
    def __init__(self, calculation=None):
        Queue.__init__(self, calculation)
        self.opers = Stack()
        self.digits = Stack()

    def set_calculation(self, calculation):
        self.__init__(calculation)

    def show_calculation(self):
        self.show_queue()

    def sort_calculation(self):
        rslt = None  # 'La cadena del cálculo es inválida.'
        calculation = 0

        if not self.queue_empty():
            while not self.queue_empty():
                element = self.dequeue()

                if not element == ' ':
                    if element in ('+', '-', '*', '/'):
                        self.opers.push(element)
                    elif element.isdigit():
                        self.digits.push(element)
                    else:
                        rslt = 'La cadena del cálculo es inválida.'
                        break

            if rslt is not None and not (self.opers.stack_empty() or self.digits.stack_empty()):
                print('Stack de Números: %s' % str(self.digits.return_stack()))
                print('Stack de Operandos: %s' % str(self.opers.return_stack()))

                while not self.digits.stack_empty():
                    left_digit = self.digits.pop()

                    if not self.opers.stack_empty():
                        oper = self.opers.pop()

                        if not self.digits.stack_empty():
                            right_digit = self.digits.pop()

                            if oper == '+':
                                calculation += float(right_digit) + float(left_digit)
                            elif oper == '-':
                                calculation -= float(right_digit) + float(left_digit)
                            elif oper == '*':
                                calculation *= float(right_digit) * float(left_digit)
                            elif oper == '/':
                                calculation /= float(right_digit) / float(left_digit)
                        else:
                            break
                    else:
                        rslt = ''
                        break
        else:
            rslt = 'No hay un cálculo para procesar.'

        if rslt is not None:
            print(rslt)
        else:
            print('El resultado del cálculo es %s' % str(rslt))
