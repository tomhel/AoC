#!/usr/bin/env python3


def parse_wire(wire):
    for instr in wire.split(","):
        yield instr[:1], int(instr[1:])


def plot_wire(wire):
    x, y = 0, 0

    for direction, length in wire:
        if direction == "U":
            dy, dx = 1, 0
        elif direction == "D":
            dy, dx = -1, 0
        elif direction == "L":
            dy, dx = 0, -1
        elif direction == "R":
            dy, dx = 0, 1
        else:
            raise Exception("unknown direction: %s" % direction)

        for _ in range(length):
            x += dx
            y += dy
            yield x, y


data = list(open("input"))
plot1 = plot_wire(parse_wire(data[0]))
plot2 = plot_wire(parse_wire(data[1]))
intersections = set(plot1).intersection(set(plot2))

print(min(abs(x) + abs(y) for x, y in intersections))

