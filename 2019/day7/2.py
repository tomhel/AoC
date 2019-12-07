#!/usr/bin/env python3


import itertools
import threading
import queue


def read_value(pc, prog, mode):
    if mode == 0:
        return prog[prog[pc]]
    elif mode == 1:
        return prog[pc]
    else:
        raise Exception("unknown mode: %d" % mode)


def write_value(pc, prog, mode, value):
    if mode != 0:
        raise Exception("only position mode for writes: %d" % mode)
    prog[prog[pc]] = value


def execute(prog, input_pipe, output_pipe, pid):
    pc = 0

    while True:
        op = int(str(prog[pc])[-2:])
        modes = [int(m) for m in str(prog[pc])[:-2].rjust(3, "0")]

        if op == 1:
            v1 = read_value(pc + 1, prog, modes[2])
            v2 = read_value(pc + 2, prog, modes[1])
            write_value(pc + 3, prog, modes[0], v1 + v2)
            pc += 4
        elif op == 2:
            v1 = read_value(pc + 1, prog, modes[2])
            v2 = read_value(pc + 2, prog, modes[1])
            write_value(pc + 3, prog, modes[0], v1 * v2)
            pc += 4
        elif op == 3:
            v1 = input_pipe.get()
            print("[%d]>>> %d" % (pid, v1))
            write_value(pc + 1, prog, modes[2], v1)
            pc += 2
        elif op == 4:
            v1 = read_value(pc + 1, prog, modes[2])
            print("[%d] %d" % (pid, v1))
            output_pipe.put(v1)
            pc += 2
        elif op == 5:
            v1 = read_value(pc + 1, prog, modes[2])
            if v1 != 0:
                pc = read_value(pc + 2, prog, modes[1])
            else:
                pc += 3
        elif op == 6:
            v1 = read_value(pc + 1, prog, modes[2])
            if v1 == 0:
                pc = read_value(pc + 2, prog, modes[1])
            else:
                pc += 3
        elif op == 7:
            v1 = read_value(pc + 1, prog, modes[2])
            v2 = read_value(pc + 2, prog, modes[1])
            write_value(pc + 3, prog, modes[0], int(v1 < v2))
            pc += 4
        elif op == 8:
            v1 = read_value(pc + 1, prog, modes[2])
            v2 = read_value(pc + 2, prog, modes[1])
            write_value(pc + 3, prog, modes[0], int(v1 == v2))
            pc += 4
        elif op == 99:
            break
        else:
            raise Exception("unknown op: %d" % op)


def run_permutations(prog):
    for seq in itertools.permutations(range(5, 10)):
        pipe1 = queue.Queue()
        pipe2 = queue.Queue()
        pipe3 = queue.Queue()
        pipe4 = queue.Queue()
        pipe5 = queue.Queue()

        pipe_inputs = [pipe1, pipe2, pipe3, pipe4, pipe5]
        pipe_outputs = [pipe2, pipe3, pipe4, pipe5, pipe1]

        threads = []

        for i, pipe_in, pipe_out, ampinput in zip(range(5), pipe_inputs, pipe_outputs, seq):
            pipe_in.put(ampinput)

            if i == 0:
                pipe_in.put(0)

            t = threading.Thread(
                target=execute, 
                args=(prog[:], pipe_in, pipe_out, i)
            )
            threads.append(t)

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        yield pipe1.get()


program = [int(i) for i in open("input").read().split(",")]
print(max(run_permutations(program)))
