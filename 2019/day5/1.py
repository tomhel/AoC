#!/usr/bin/env python3


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


def execute(prog):
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
            print(">>> ", end="")
            v1 = int(input())
            write_value(pc + 1, prog, modes[2], v1)
            pc += 2
        elif op == 4:
            v1 = read_value(pc + 1, prog, modes[2])
            print(v1)
            pc += 2
        elif op == 99:
            break
        else:
            raise Exception("unknown op: %d" % op)


program = [int(i) for i in open("input").read().split(",")]
execute(program)

