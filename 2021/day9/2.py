from functools import reduce
import operator


def load():
    with open("input") as f:
        data = {}

        for y, row in enumerate(f):
            data.update({(x, y): int(z) for x, z in enumerate(list(row.strip()))})

        return data


def get_adjacent_height(pos, heightmap):
    x, y = pos

    for p in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        z = heightmap.get(p)

        if z is not None:
            yield z


def get_basin(pos, heightmap, basin):
    z = heightmap.get(pos)

    if z is None or z == 9 or pos in basin:
        return basin

    basin.add(pos)
    x, y = pos

    for p in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        get_basin(p, heightmap, basin)

    return basin


def find_basins():
    heightmap = load()
    low_points = []

    for pos in heightmap:
        z = heightmap.get(pos)
        if min(get_adjacent_height(pos, heightmap)) > z:
            low_points.append(pos)

    basins = []

    for pos in low_points:
        basins.append(len(get_basin(pos, heightmap, set())))

    return reduce(operator.mul, sorted(basins)[-3:], 1)


print(find_basins())
