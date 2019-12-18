#!/usr/bin/env python3


import intcode


def capture_camera(out_buffer):
    x, y = 0, 0
    capture = {}

    for a in out_buffer:
        if a == 10:
            y += 1
            x = 0
            continue

        capture[(x, y)] = chr(a)
        x += 1

    return capture


def calc_alignment_params(out_buffer):
    scaffold = ("#", "<", ">", "v", "^")
    capture = capture_camera(out_buffer)

    for c, v in capture.items():
        if v not in scaffold:
            continue

        x, y = c
        intersection = True

        for a, b in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            if capture.get((x + a, y + b), ".") not in scaffold:
                intersection = False
                break

        if intersection:
            yield x * y


def run_ascii():
    computer = intcode.Computer(intcode.load_program("input"), intcode.BufferIOHandler())
    computer.execute()
    out_buffer = computer.get_output()
    return sum(calc_alignment_params(out_buffer))


print(run_ascii())
