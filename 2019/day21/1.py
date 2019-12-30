#!/usr/bin/env python3


import intcode
import queue


def deploy_springdroid():
    computer = intcode.Computer(intcode.load_program("input"), intcode.BufferIOHandler())

    computer.input_text("NOT C J\n")
    computer.input_text("AND D J\n")
    computer.input_text("NOT A T\n")
    computer.input_text("OR T J\n")
    computer.input_text("WALK\n")

    computer.execute()
    computer.print_output()


deploy_springdroid()
