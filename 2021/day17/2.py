import math


def load():
    with open("input") as f:
        _, _, xrange, yrange = next(f).strip().split(" ")
        x1, x2 = xrange[2:][:-1].split("..")
        yield int(x1), int(x2)
        y1, y2 = yrange[2:].split("..")
        yield int(y1), int(y2)


def is_target_hit(x, y, target_x, target_y):
    x1, x2 = target_x
    y1, y2 = target_y
    return x1 <= x <= x2 and y1 <= y <= y2


def is_target_miss(x, y, target_x, target_y):
    x1, x2 = target_x
    y1, y2 = target_y
    return x > x2 or y < y1


def launch_probe(dx, dy, target_x, target_y):
    max_height = -math.inf
    x, y = 0, 0

    while True:
        if is_target_miss(x, y, target_x, target_y):
            return -math.inf
        elif is_target_hit(x, y, target_x, target_y):
            return max_height

        x, y = x + dx, y + dy
        max_height = max(max_height, y)
        dx = dx - 1 if dx > 0 else dx
        dx = dx + 1 if dx < 0 else dx
        dy -= 1


def num_init_values():
    target_x, target_y = list(load())
    count = 0

    for dx in range(1, target_x[1] + 1):
        for dy in range(-abs(target_y[0]), abs(target_y[0])):
            count += launch_probe(dx, dy, target_x, target_y) != -math.inf

    return count


print(num_init_values())
