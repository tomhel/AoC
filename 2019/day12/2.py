#!/usr/bin/env python3


import re
import itertools


class Pattern(object):
    def __init__(self):
        self.sequence = []
        self.pattern = []
        self.confidence = 1.5

    def _get_in_pattern(self, i):
        if len(self.pattern) == 0:
            return None

        return self.pattern[i % len(self.pattern)]

    def add(self, v):
        self.sequence.append(v)
        i = len(self.sequence) - 1
        p = self._get_in_pattern(i)

        if v != p:
            for j in range(len(self.pattern), i):
                self.pattern.append(self.sequence[j])

            p = self._get_in_pattern(i)
            if v != p:
                self.pattern.append(self.sequence[i])

    def found(self):
        return len(self.sequence) > int(len(self.pattern) * self.confidence) + 1

    def length(self):
        return len(self.pattern)


def add_to_patterns(moons, patterns):
    for i, m in moons.items():
        for j, c in enumerate(itertools.chain(m[0], m[1])):
            patterns[i*6+j].add(c)


def calc_least_common_multiple(divisors):
    lcm = max(divisors)

    for divisor in divisors:
        if lcm % divisor == 0:
            continue
        for factor in range(2, divisor + 1):
            if (lcm * factor) % divisor == 0:
                lcm *= factor
                break

    return lcm


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


def simulate(moons):
    patterns = [Pattern() for _ in range(len(moons) * 6)]
    add_to_patterns(moons, patterns)

    while True:
        apply_gravity(moons)
        apply_velocity(moons)
        add_to_patterns(moons, patterns)
        found = True

        for pattern in patterns:
            if not pattern.found():
                found = False
                break

        if found:
            return calc_least_common_multiple([p.length() for p in patterns])


data = {i: ([int(x), int(y), int(z)], [0, 0, 0])
        for i, x, y, z in ((i, *re.findall("-?\d+", a))
                           for i, a in enumerate(open("input")))}
print(simulate(data))
