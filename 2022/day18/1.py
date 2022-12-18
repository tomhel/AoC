def load():
    with open("input") as f:
        for row in f:
            yield tuple(int(x) for x in row.strip().split(","))


def surface_area():
    cubes = set(load())
    count = 0
    for x, y, z in cubes:
        for dx, dy, dz in ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)):
            if (x + dx, y + dy, z + dz) not in cubes:
                count += 1
    return count


print(surface_area())
