#!/usr/bin/env python3


import math


def plot_asteroids(grid):
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "#":
                yield x, y


def count_visibility(plot):
    for x, y in plot:
        blocked_angles = set()
        count = 0

        for a, b in plot:
            if (x, y) == (a, b):
                continue

            if y == b:
                angle = -math.pi / 2 if a > x else math.pi / 2
            else:
                angle = math.atan(float(x - a) / float(y - b))

                if b > y:
                    angle += math.pi

            if angle not in blocked_angles:
                blocked_angles.add(angle)
                count += 1

        yield count, (x, y)
        

data = [list(x.strip()) for x in open("input")]
print(max(count_visibility(list(plot_asteroids(data)))))
