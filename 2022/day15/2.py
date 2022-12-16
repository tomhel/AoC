import re


def load():
    with open("input") as f:
        for row in f:
            m = re.match(r".*x=(-?\d+), y=(-?\d+):.+x=(-?\d+), y=(-?\d+)$", row)
            yield (int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))


def find_distress_beacon():
    report = list(load())
    maxx, maxy = 4000000, 4000000  # change this to 20 if running on test input
    y = 0
    while y <= maxy:
        x = 0
        while x <= maxx:
            found = True
            for sensor, beacon in report:
                sx, sy = sensor
                bx, by = beacon
                dx, dy = abs(sx - bx), abs(sy - by)
                dxx, dyy = abs(sx - x), abs(sy - y)
                if dxx + dyy <= dx + dy:
                    x += dx + dy + sx - x - dyy
                    found = False
                    break
            if found:
                return x, y
            x += 1
        y += 1


def determine_tuning_frequency():
    x, y = find_distress_beacon()
    return x * 4000000 + y


# takes about 60 seconds to run.
print(determine_tuning_frequency())
