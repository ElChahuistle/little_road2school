# Esta instruncción se ve medio rara, porque pareciera que importa dos veces
# la misma clase. Sin embargo, la parte "from Queue" se refiere al nombre del archivo (Queue.py)
# y la parte "import Queue" se refiere propiamente a la clase que se declarado dentro del archivo.
from Queue import Queue


class RoundRobin:
    # Queue de procesos a ejecutarse.
    processes = Queue()

    # Este atributo será un constante; las constantes siempre se nombran en mayúsculas
    # para reconocerlas de los atributos que son variables.
    MAX_EXEC_TIME = 100
    # Simularemos la ejecución de cada proceso en bloques de 10.
    EXEC_BLOCKS = 10

    def processes_queue_size(self):
        return self.processes.queue_size()

    def process_queue_empty(self):
        return self.processes_queue_size() == 0 if True else False

    # Este método agrega un proceso con su tiempo de ejecución al queue de procesos.
    # Lo que finalmente guarda el queue es un tipo de dato standard de Python llamado "tuple",
    # que es un conjunto de datos agrupados.
    def add_process(self, process_name, proc_exec_time):
        self.processes.queue_element([process_name, proc_exec_time])

    def get_next_process(self):
        return self.processes.dequeue_element()

    def show_processes_queue(self):
        proc_num = 0

        while proc_num < self.processes_queue_size():
            proc_num += 1
            proc, time = self.get_next_process()

            print('%i. %s (Exec. Time %r)' % (proc_num, proc, time))

            self.add_process(proc, time)

    def execute_process(self):
        print('Comenzar Ejecución...')
        print('Hay %i procesos para ejecutar.' % self.processes_queue_size())

        # Con este while controlamos la ejecución de todos los procesos en el queue.
        # Así que mientras haya procesos en el queue este while se ciclará indefinidamente.
        while not self.process_queue_empty():
            # Obtenemos el primer proceso disponible en el queue.
            process_name, proc_exec_time = self.get_next_process()

            print('Ejecución de "%s".' % process_name)

            # Dado que cada proceso sólo puede ejecutarse por determinado tiempo,
            # comparar "proc_exec_time" con "MAX_EXEC_TIME".
            if proc_exec_time <= self.MAX_EXEC_TIME:
                print('-> Tiempo de ejecución es *menor* de MAX.')

                # Si el tiempo de ejecución del proceso es menor o igual al tiempo
                # máximo de ejecución, entonces se procesará completamente.
                exec_time = proc_exec_time
                proc_exec_time = 0
            else:
                print('-> Tiempo de ejecución es **MAYOR** de MAX.')

                # Si el tiempo de ejecución del proceso es mayor al tiempo máximo de ejecución,
                # entonces se ejecuta el tiempo máximo y el remanente de ejecución es la diferencia
                # entre el máximo de ejecución y el tiempo original de ejecución del proceso.
                exec_time = self.MAX_EXEC_TIME
                proc_exec_time -= self.MAX_EXEC_TIME

                # Dado que este es el caso en que el tiempo de ejecución del proceso es mayor
                # al máximo tiempo de ejecución, devolvemos el proceso al queue de procesos.
                self.add_process(process_name, proc_exec_time)

            # Esta variable es sólo poder mostrar el número de iteraciones que se hacen para cada proceso.
            # Esta variable se reiniciará en 0 cada vez que se tome un proceso del queue de procesos.
            iteration = 1

            # Ejecutar el proceso hasta el tiempo de ejecución que se determinó antes.
            while exec_time > 0:
                # Simularemos que la ejecución será en bloques.
                exec_time -= self.EXEC_BLOCKS

                # Aunque se puede usar "+" para concatenar valores a desplegarse en un string, la
                # siguiente forma es la correcta, que es usando "wild cards" como %s (para strings)
                # y %i para enteros; en el caso de números reales sería %r.
                # Después del string a desplegar viene una tupla de los valores a pasarse a cada
                # "wild card" declarada antes.

                iteration += 1

            print('Tiempo restante de ejecución para este proceso: %i.' % proc_exec_time)
            print()


if __name__ == '__main__':
    round_robin = RoundRobin()

    round_robin.add_process('Process, process on the wall', 99)
    round_robin.add_process('Oh process, where are you?', 101)

    print()
    round_robin.show_processes_queue()

    print()
    print('Número de procesos en el queue: %i.' % round_robin.processes_queue_size())

    print()
    round_robin.execute_process()

    round_robin.add_process('Process ONE', 101)
    round_robin.add_process('Process TWO', 99)
    round_robin.add_process('Process THREE', 250)
    round_robin.add_process('Process FOUR', 57)

    print()
    round_robin.show_processes_queue()

    print()
    print('Número de procesos en el queue: %i.' % round_robin.processes_queue_size())

    print()
    round_robin.execute_process()
