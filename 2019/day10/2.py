#!/usr/bin/env python3


import math


def plot_asteroids(grid):
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "#":
                yield x, y


def count_visibility(plot):
    for origin in plot:
        blocked_angles = set()
        count = 0

        for asteroid in plot:
            if origin == asteroid:
                continue

            angle, _, _, _ = measure_asteroid(asteroid, origin)

            if angle not in blocked_angles:
                blocked_angles.add(angle)
                count += 1

        yield count, origin


def analyze_asteroids(plot, origin):
    for asteroid in plot:
        if origin == asteroid:
            continue

        yield measure_asteroid(asteroid, origin)


def measure_asteroid(asteroid, origin):
    a, b = asteroid
    x, y = origin

    if y == b:
        angle = math.pi / 2 if a > x else math.pi + math.pi / 2
    else:
        angle = math.atan(float(a - x) / float(y - b))

        if b > y:
            angle += math.pi
        elif x > a and y > b:
            angle += math.pi * 2

    distance = math.sqrt((a - x) ** 2 + (y - b) ** 2)
    return angle, distance, a, b


def find_visible_asteroids(plot):
    return sorted({a: (a, d, x, y) for a, d, x, y in sorted(plot, reverse=True)}.values())


def vaporize(plot):
    _, best_pos = max(count_visibility(plot))

    while len(plot) > 1:
        for _, _, x, y in find_visible_asteroids(analyze_asteroids(plot, best_pos)):
            plot.remove((x, y))
            yield (x, y)


data = [list(x.strip()) for x in open("input")]
asteroids = set(plot_asteroids(data))
asteroid_200 = list(vaporize(asteroids))[199]
print(asteroid_200[0] * 100 + asteroid_200[1])
