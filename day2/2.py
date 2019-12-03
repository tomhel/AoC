#!/usr/bin/env python3


def execute(prog):
    pc = 0

    while True:
        op = prog[pc]

        if op == 1:
            r = prog[prog[pc + 1]] + prog[prog[pc + 2]]
            prog[prog[pc + 3]] = r
            pc += 4
        elif op == 2:
            r = prog[prog[pc + 1]] * prog[prog[pc + 2]]
            prog[prog[pc + 3]] = r
            pc += 4
        elif op == 99:
            break
        else:
            raise Exception("unknown op: %d" % op)


def find_init_values(prog):
    for noun in range(100):
        for verb in range(100):
            p = prog[:]
            p[1] = noun
            p[2] = verb
            execute(p)
            if p[0] == 19690720:
                return noun, verb


program = [int(i) for i in open("input").read().split(",")]

print("%02d%02d" % find_init_values(program))
