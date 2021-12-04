def load():
    with open("input") as f:
        for x in f:
            yield int(x.strip())


def calc_depth_increase():
    measurements = list(load())
    prev = measurements[0]
    inc = 0

    for depth in measurements[1:]:
        inc += depth > prev
        prev = depth

    return inc


print(calc_depth_increase())
