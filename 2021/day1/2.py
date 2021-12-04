def load():
    with open("input") as f:
        for x in f:
            yield int(x.strip())


def calc_depth_increase():
    measurements = list(load())
    prev = sum(measurements[:3])
    inc = 0

    for i in range(1, len(measurements)):
        depth = sum(measurements[i:i+3])
        inc += depth > prev
        prev = depth

    return inc


print(calc_depth_increase())
