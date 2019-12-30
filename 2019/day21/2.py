#!/usr/bin/env python3


import intcode


def deploy_springdroid():
    computer = intcode.Computer(intcode.load_program("input"), intcode.BufferIOHandler())

    computer.input_text("NOT C J\n")
    computer.input_text("AND D J\n")
    computer.input_text("AND H J\n")
    computer.input_text("NOT A T\n")
    computer.input_text("OR T J\n")
    computer.input_text("NOT B T\n")
    computer.input_text("AND D T\n")
    computer.input_text("OR T J\n")
    computer.input_text("RUN\n")

    computer.execute()
    computer.print_output()


deploy_springdroid()
