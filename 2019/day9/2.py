#!/usr/bin/env python3


import itertools


def read_value(pc, mem, mode, relbase):
    if mode == 0:
        return mem.get(mem.get(pc, 0), 0)
    elif mode == 1:
        return mem.get(pc, 0)
    elif mode == 2:
        return mem.get(mem.get(pc, 0) + relbase, 0)
    else:
        raise Exception("unsupported mode for reads: %d" % mode)


def write_value(pc, mem, mode, value, relbase):
    if mode == 0:
        mem[mem.get(pc, 0)] = value
    elif mode == 2:
        mem[mem.get(pc, 0) + relbase] = value
    else:
        raise Exception("unsupported mode for writes: %d" % mode)
 

def execute(prog, inputdata):
    pc = 0
    relbase = 0
    mem = {i: v for i, v in enumerate(prog)}
    outputdata = []
    inputdata = iter(inputdata)

    while True:
        op = int(str(mem[pc])[-2:])
        modes = [int(m) for m in str(mem[pc])[:-2].rjust(3, "0")]

        if op == 1:
            v1 = read_value(pc + 1, mem, modes[2], relbase)
            v2 = read_value(pc + 2, mem, modes[1], relbase)
            write_value(pc + 3, mem, modes[0], v1 + v2, relbase)
            pc += 4
        elif op == 2:
            v1 = read_value(pc + 1, mem, modes[2], relbase)
            v2 = read_value(pc + 2, mem, modes[1], relbase)
            write_value(pc + 3, mem, modes[0], v1 * v2, relbase)
            pc += 4
        elif op == 3:
            v1 = int(next(inputdata))
            print(">>> %d" % v1)
            write_value(pc + 1, mem, modes[2], v1, relbase)
            pc += 2
        elif op == 4:
            v1 = read_value(pc + 1, mem, modes[2], relbase)
            print(v1)
            outputdata.append(v1)
            pc += 2
        elif op == 5:
            v1 = read_value(pc + 1, mem, modes[2], relbase)
            if v1 != 0:
                pc = read_value(pc + 2, mem, modes[1], relbase)
            else:
                pc += 3
        elif op == 6:
            v1 = read_value(pc + 1, mem, modes[2], relbase)
            if v1 == 0:
                pc = read_value(pc + 2, mem, modes[1], relbase)
            else:
                pc += 3
        elif op == 7:
            v1 = read_value(pc + 1, mem, modes[2], relbase)
            v2 = read_value(pc + 2, mem, modes[1], relbase)
            write_value(pc + 3, mem, modes[0], int(v1 < v2), relbase)
            pc += 4
        elif op == 8:
            v1 = read_value(pc + 1, mem, modes[2], relbase)
            v2 = read_value(pc + 2, mem, modes[1], relbase)
            write_value(pc + 3, mem, modes[0], int(v1 == v2), relbase)
            pc += 4
        elif op == 9:
            v1 = read_value(pc + 1, mem, modes[2], relbase)
            relbase += v1
            pc += 2
        elif op == 99:
            break
        else:
            raise Exception("unknown op: %d" % op)

    return outputdata
        

program = [int(i) for i in open("input").read().split(",")]
execute(program, [2])
