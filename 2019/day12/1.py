#!/usr/bin/env python3


import re
import itertools


def apply_gravity(moons):
    for m1, m2 in itertools.combinations(moons, 2):
        pos1, vel1 = moons[m1]
        pos2, vel2 = moons[m2]

        for i in range(3):
            dv = (pos1[i] - pos2[i]) // max(abs(pos1[i] - pos2[i]), 1)
            vel1[i] -= dv
            vel2[i] += dv


def apply_velocity(moons):
    for pos, vel in moons.values():
        for i in range(3):
            pos[i] += vel[i]


def simulate(moons, steps):
    for t in range(steps):
        apply_gravity(moons)
        apply_velocity(moons)

    return sum(sum(abs(p) for p in pos) * sum(abs(v) for v in vel) for pos, vel in moons.values())


data = {i: ([int(x), int(y), int(z)], [0, 0, 0])
        for i, x, y, z in ((i, *re.findall("-?\d+", a))
                           for i, a in enumerate(open("input")))}
print(simulate(data, 1000))
