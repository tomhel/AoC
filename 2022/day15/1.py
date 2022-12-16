import math
import re


def load():
    with open("input") as f:
        for row in f:
            m = re.match(r".*x=(-?\d+), y=(-?\d+):.+x=(-?\d+), y=(-?\d+)$", row)
            yield (int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))


def positions_without_beacons():
    report = list(load())
    minx, maxx = math.inf, -math.inf
    for sensor, beacon in report:
        minx = min(minx, beacon[0], sensor[0])
        maxx = max(maxx, beacon[0], sensor[0])
    y = 2000000  # change this to 10 if running on test input
    count = 0
    for x in range(minx, maxx):
        for sensor, beacon in report:
            sx, sy = sensor
            bx, by = beacon
            if (sx == x and sy == y) or (bx == x and by == y):
                break
            elif abs(sx - x) + abs(sy - y) <= abs(sx - bx) + abs(sy - by):
                count += 1
                break
    return count


# takes about 30 seconds to run, only 2 seconds with pypy
print(positions_without_beacons())
