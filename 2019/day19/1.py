#!/usr/bin/env python3


import intcode


def deploy_drones():
    prog = intcode.load_program("input")
    count = 0

    for x in range(50):
        for y in range(50):
            computer = intcode.Computer(prog[:], intcode.BufferIOHandler([x, y]))
            computer.execute()
            count += computer.get_output()[0]

    return count


print(deploy_drones())
