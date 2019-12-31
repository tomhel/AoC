#!/usr/bin/env python3


import intcode
import re


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


def get_rotation(facing, dx, dy):
    directions = {
        (-1, 0): "<",
        (1, 0): ">",
        (0, 1): "v",
        (0, -1): "^"
    }
    new_facing = directions[(dx, dy)]

    if facing == "<":
        return ("R", "^") if new_facing == "^" else ("L", "v")
    elif facing == ">":
        return ("L", "^") if new_facing == "^" else ("R", "v")
    elif facing == "^":
        return ("L", "<") if new_facing == "<" else ("R", ">")
    elif facing == "v":
        return ("R", "<") if new_facing == "<" else ("L", ">")


def get_movement_sequence(pos, facing, capture, visited):
    x, y = pos
    seq = []
    trace = set()

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        a, b = x + dx, y + dy

        if capture.get((a, b), ".") != "#":
            continue
        elif (a, b) in visited:
            continue

        while capture.get((a + dx, b + dy), ".") == "#":
            a, b = a + dx, b + dy
            trace.add((a, b))

        rotation, facing = get_rotation(facing, dx, dy)
        seq.append(rotation)
        seq.append(str(len(trace) + 1))
        capture[pos] = "#"
        capture[(a, b)] = facing
        break

    return seq, trace


def build_path(capture):
    path = []
    trace = set()

    while True:
        pos, facing = [(p, v) for p, v in capture.items() if v in ("<", ">", "v", "^")][0]
        seq, trace = get_movement_sequence(pos, facing, capture, trace)

        if len(seq) == 0:
            break

        path.extend(seq)

    return path


def identify_subroutines(path):
    pathstr = "".join(path)
    subroutines = []
    functions = ["A", "B", "C"]
    start = 0

    while len(subroutines) < len(functions):
        for i in range(20, 0, -1):
            routine = pathstr[start:i]

            if len(routine) == 0:
                continue
            elif not routine[-1].isdigit():
                continue
            elif len(set(routine).intersection(set(functions))) > 0:
                continue

            if pathstr.count(routine) > 1:
                pathstr = pathstr.replace(routine, functions[len(subroutines)])
                subroutines.append(routine)
                start = 0
                break

        start += 1

    return list(pathstr), [re.findall("[RL]|\d+", r) for r in subroutines]


def encode_input(data):
    return [ord(c) for c in ",".join(data) + "\n"]


def print_ascii(data):
    for i in data:
        if 0 <= i <= 127:
            print(chr(i), end="")
        else:
            print(i)


def vacuum_scaffold():
    prog = intcode.load_program("input")
    computer = intcode.Computer(prog[:], intcode.BufferIOHandler())
    computer.execute()
    capture = capture_camera(computer.get_output())

    callorder, subroutines = identify_subroutines(build_path(capture))
    input_logic = encode_input(callorder) + \
                  encode_input(subroutines[0]) + encode_input(subroutines[1]) + encode_input(subroutines[2]) + \
                  encode_input(["n"])

    prog[0] = 2
    computer = intcode.Computer(prog[:], intcode.BufferIOHandler(input_logic))
    computer.execute()
    print_ascii(computer.get_output())


vacuum_scaffold()
