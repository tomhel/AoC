#!/usr/bin/env python3


import queue


class TerminalIOHandler(object):

    def __init__(self):
        pass

    def read(self):
        return int(input(">>> "))

    def write(self, v):
        print(v)

    def dump_output(self):
        return []

    def exit(self):
        pass


class BufferIOHandler(object):

    def __init__(self, input_values=None):
        self.in_buffer = iter(input_values[:] if input_values is not None else [])
        self.out_buffer = []

    def read(self):
        return next(self.in_buffer)

    def write(self, v):
        self.out_buffer.append(v)

    def dump_output(self):
        return self.out_buffer

    def exit(self):
        pass


class PipeIOHandler(object):

    def __init__(self, in_pipe, out_pipe, input_values=None):
        self.in_pipe = in_pipe
        self.out_pipe = out_pipe
        if input_values is not None:
            for v in input_values:
                self.in_pipe.put(v)

    def read(self):
        v = self.in_pipe.get()
        self.in_pipe.task_done()
        return v

    def write(self, v):
        self.out_pipe.put(v)

    def dump_output(self):
        dump = []

        while True:
            try:
                v = self.out_pipe.get_nowait()
                if v is not None:
                    dump.append(v)
            except queue.Empty:
                break

        return dump

    def exit(self):
        self.out_pipe.put(None)


def load_program(path):
    with open(path) as f:
        return [int(i) for i in f.read().split(",")]


class Computer(object):

    def __init__(self, program, io_handler):
        self.pc = 0
        self.rel_base = 0
        self.mem = {adr: i for adr, i in enumerate(program)}
        self.io_handler = io_handler

    def _read_value(self, adr, mode):
        if mode == 0:  # position
            return self.mem.get(self.mem.get(adr, 0), 0)
        elif mode == 1:  # immediate
            return self.mem.get(adr, 0)
        elif mode == 2:  # relative
            return self.mem.get(self.mem.get(adr, 0) + self.rel_base, 0)
        else:
            raise Exception("unsupported mode for reads: %d" % mode)

    def _write_value(self, adr, mode, value):
        if mode == 0:  # position
            self.mem[self.mem.get(adr, 0)] = value
        elif mode == 2:  # relative
            self.mem[self.mem.get(adr, 0) + self.rel_base] = value
        else:
            raise Exception("unsupported mode for writes: %d" % mode)

    def execute(self):
        while True:
            op = int(str(self.mem[self.pc])[-2:])
            modes = [int(m) for m in str(self.mem[self.pc])[:-2].rjust(3, "0")]

            if op == 1:  # add
                v1 = self._read_value(self.pc + 1, modes[2])
                v2 = self._read_value(self.pc + 2, modes[1])
                self._write_value(self.pc + 3, modes[0], v1 + v2)
                self.pc += 4
            elif op == 2:  # multiply
                v1 = self._read_value(self.pc + 1, modes[2])
                v2 = self._read_value(self.pc + 2, modes[1])
                self._write_value(self.pc + 3, modes[0], v1 * v2)
                self.pc += 4
            elif op == 3:  # input
                v1 = self.io_handler.read()
                self._write_value(self.pc + 1, modes[2], v1)
                self.pc += 2
            elif op == 4:  # output
                v1 = self._read_value(self.pc + 1, modes[2])
                self.io_handler.write(v1)
                self.pc += 2
            elif op == 5:  # jump if not zero
                v1 = self._read_value(self.pc + 1, modes[2])
                self.pc = self._read_value(self.pc + 2, modes[1]) if v1 != 0 else self.pc + 3
            elif op == 6:  # jump if zero
                v1 = self._read_value(self.pc + 1, modes[2])
                self.pc = self._read_value(self.pc + 2, modes[1]) if v1 == 0 else self.pc + 3
            elif op == 7:  # less than
                v1 = self._read_value(self.pc + 1, modes[2])
                v2 = self._read_value(self.pc + 2, modes[1])
                self._write_value(self.pc + 3, modes[0], int(v1 < v2))
                self.pc += 4
            elif op == 8:  # equal
                v1 = self._read_value(self.pc + 1, modes[2])
                v2 = self._read_value(self.pc + 2, modes[1])
                self._write_value(self.pc + 3, modes[0], int(v1 == v2))
                self.pc += 4
            elif op == 9:  # adjust relative base
                v1 = self._read_value(self.pc + 1, modes[2])
                self.rel_base += v1
                self.pc += 2
            elif op == 99:  # quit
                break
            else:
                raise Exception("unknown op: %d" % op)

        self.io_handler.exit()

    def get_output(self):
        return self.io_handler.dump_output()
