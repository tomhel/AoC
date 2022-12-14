def load():
    with open("input") as f:
        for row in f:
            yield [[int(i) for i in x.strip().split(",")] for x in row.split("->")]


def construct_cave(paths):
    cave = {}
    for path in paths:
        for i in range(len(path) - 1):
            x, y = path[i]
            a, b = path[i + 1]
            dx, dy = 0 if a - x == 0 else (a - x) // abs(a - x), 0 if b - y == 0 else (b - y) // abs(b - y)
            cave[(x, y)] = "#"
            while x != a or y != b:
                x, y = x + dx, y + dy
                cave[(x, y)] = "#"
    return cave


def count_units_of_sand():
    cave = construct_cave(load())
    start_x, start_y = 500, 0
    minx = min([x for x, _ in cave] + [start_x])
    maxx, maxy = max([x for x, _ in cave] + [start_x]), max([y for _, y in cave] + [start_y])
    count, x, y = 0, start_x, start_y
    while minx <= x <= maxx and y <= maxy:
        at_rest = True
        for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
            a, b = x + dx, y + dy
            if cave.get((a, b)) is None:
                x, y = a, b
                at_rest = False
                break
        if at_rest:
            count += 1
            cave[(x, y)] = "o"
            x, y = start_x, start_y
    return count


print(count_units_of_sand())
