from __future__ import annotations
from DataStructures import Stack, Queue


class Process:
    def __init__(self, process_name: str = None, exec_time: int = None):
        self.process_name = process_name
        self.exec_time = exec_time
        self.sub_process = None

    def set_process(self, process_name: str, exec_time: int):
        self.__init__(process_name, exec_time)

    def set_sub_process(self, sub_process_name: str = None, sub_exec_time: float = None):
        self.exec_time += sub_exec_time
        self.sub_process = Process(sub_process_name, sub_exec_time)

    def set_exec_time(self, time: float):
        self.exec_time = time

    def get_exec_time(self) -> float:
        return self.exec_time

    def get_sub_process(self) -> Process:
        sub_process = self.sub_process
        self.sub_process = None

        return sub_process

    def get_process_name(self) -> str:
        return self.process_name

    def remove_sub_process(self):
        self.exec_time -= self.sub_process.exec_time
        self.sub_process = None

    def has_sub_process(self) -> bool:
        return self.sub_process is not None if True else False

    def show_process(self):
        print('Process: %s (Exec. Time: %r)' % (self.process_name, self.exec_time))

        if self.sub_process is not None:
            print('--> Sub-process: %s (Exec. Time: %r)' % (self.sub_process.process_name, self.sub_process.exec_time))


class RoundRobinPlus(Stack, Queue):
    MAX_EXEC_TIME = 50
    MAX_BLOCKS = 5

    def add_process(self, proc: Process):
        self.queue(proc)

    def get_process(self) -> Process:
        return self.dequeue()

    def hold_process(self, proc: Process, sub_process_name: str):
        self.push(tuple([proc, sub_process_name]))

    def bring_process(self) -> Process:
        return self.pop()

    def check_for_parent(self, sub_process_name: str):
        process, stck_sub_process_name = self.bring_process()

        if stck_sub_process_name == sub_process_name:
            self.add_process(process)
        else:
            self.hold_process(process, stck_sub_process_name)

    def show_processes_queue(self):
        index = 0

        while index < self.queue_size():
            proc = self.get_process()
            proc.show_process()
            self.add_process(proc)

            index += 1

    def run_processes(self):
        while not self.queue_empty():
            proc = self.get_process()
            sub_proc = False
            exec_time = 0

            if proc.has_sub_process():
                sub_proc = proc.get_sub_process()
                self.hold_process(proc, sub_proc.get_process_name())
                proc = sub_proc
                sub_proc = True

            print('Process Exec. Time: %f.' % proc.get_exec_time())

            if proc.get_exec_time() <= self.MAX_EXEC_TIME:
                exec_time = proc.get_exec_time()
            else:
                exec_time = self.MAX_EXEC_TIME
                proc.set_exec_time(proc.get_exec_time() - self.MAX_EXEC_TIME)

            iteracion = 1
            while exec_time > 0:
                exec_time -= self.MAX_BLOCKS
                iteracion += 1

            # iteracion = 1
            # while exec_time <= proc.get_exec_time() and iteracion <= 10:
            #     print('Iteración %i del proceso %s.' % (iteracion, proc.get_process_name()))
            #     exec_time += self.MAX_BLOCKS
            #     iteracion += 1
            #
            # if not self.stack_empty():
            #     self.add_process(self.bring_process())


if __name__ == '__main__':
    rr = RoundRobinPlus()
    rr.add_process(Process('Process A', 10))
    rr.add_process(Process('Process B', 25))

    # process = Process('Process C', 1)
    # process.set_sub_process('Sub-Process Z', 5)
    # rr.add_process(process)
    rr.show_processes_queue()
    rr.run_processes()
