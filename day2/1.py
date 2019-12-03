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


program = [int(i) for i in open("input").read().split(",")]
program[1] = 12
program[2] = 2
execute(program)

print(program[0])
