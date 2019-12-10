#!/usr/bin/env python3


import math
from decimal import Decimal


def plot_asteroids(grid):
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "#":
                yield x, y


def count_visibility(plot):
    for x, y in plot:
        blocked_angles = set()
        count = 1

        for a, b in plot:
            if (x, y) == (a, b):
                continue

            if y == b:
                angle = -math.pi
            else:
                angle = math.atan(Decimal(x - a) / Decimal(y - b))

                if y - b < 0:
                    angle = angle + math.pi

            if angle not in blocked_angles:
                blocked_angles.add(angle)
                count += 1

        yield count, (x, y)
        

data = [list(x.strip()) for x in open("input")]
print(max(count_visibility(list(plot_asteroids(data)))))
