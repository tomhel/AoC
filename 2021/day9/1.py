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


def calc_risk_level():
    heightmap = load()
    risk = 0

    for pos in heightmap:
        z = heightmap.get(pos)

        if min(get_adjacent_height(pos, heightmap)) > z:
            risk += z + 1

    return risk


print(calc_risk_level())
