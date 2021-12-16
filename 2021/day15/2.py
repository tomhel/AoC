import math
import sys


def load():
    with open("input") as f:
        data = {}
        for x, row in enumerate(f):
            data.update({(x, y): int(r) for y, r in enumerate(row.strip())})
        return data


def find_best_path(pos, risk, cave, dest, visited, best):
    if pos == dest:
        best[pos] = risk + cave[pos]
        return risk + cave[pos]
    elif pos not in cave:
        return math.inf
    elif risk + cave[pos] >= best.get(pos, math.inf):
        return math.inf
    elif risk + cave[pos] + (dest[0] - pos[0]) + (dest[1] - pos[1]) - 1 + cave[dest] >= best.get(dest, math.inf):
        return math.inf
    elif pos not in visited:
        best[pos] = risk + cave[pos]
        visited.add(pos)
        x, y = pos
        return min(find_best_path(p, risk + cave[pos], cave, dest, set(visited), best)
                   for p in [(x, y+1), (x+1, y), (x-1, y), (x, y-1)])

    return math.inf


def transform(risk, tile_x, tile_y):
    r = (risk + tile_x + tile_y) % 9
    return 9 if r == 0 else r


def expand(cave):
    expanded = {}
    maxx, maxy = max(cave)

    for x, y in cave:
        for i in range(5):
            for j in range(5):
                expanded[(x + i * (maxx + 1), y + j * (maxy + 1))] = transform(cave[(x, y)], i, j)

    return expanded


def get_lowest_risk():
    cave = expand(load())
    start, dest = min(cave), max(cave)
    return find_best_path(start, -cave[start], cave, dest, set(), {})


# This will take around 6 hours to run...
sys.setrecursionlimit(10000)
print(get_lowest_risk())
