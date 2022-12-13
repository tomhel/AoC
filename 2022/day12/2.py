import math
import sys


def load():
    heightmap = {}
    with open("input") as f:
        for y, row in enumerate(x.strip() for x in f):
            for x, z in enumerate(row):
                heightmap[(x, y)] = z
        return heightmap


def find_path(pos, heightmap, best, visited, goals, highscore):
    visited.add(pos)
    if highscore[0] <= len(visited):
        return math.inf  # shorter path already found to another a-node.
    if best.get(pos, math.inf) <= len(visited):
        return math.inf  # shorter path already found to this node.
    if pos in goals:
        highscore[0] = len(visited)
        return len(visited) - 1
    best[pos] = len(visited)
    steps = [math.inf]
    current = heightmap[pos]
    for dx, dy in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
        a, b = pos[0] + dx, pos[1] + dy
        square = heightmap.get((a, b))
        square = "a" if square == "S" else square
        if square is None or (a, b) in visited:
            continue
        elif ord(square) + 1 >= ord("z" if current == "E" else current):
            steps.append(find_path((a, b), heightmap, best, set(visited), goals, highscore))
    return min(steps)


def minimum_steps_from_any_square():
    sys.setrecursionlimit(10**6)
    heightmap = load()
    e_node = [k for k, v in heightmap.items() if v == "E"][0]
    a_nodes = set(k for k, v in heightmap.items() if v in ("a", "S"))
    return find_path(e_node, heightmap, {}, set(), a_nodes, [math.inf])


# takes about 10 seconds to run.
print(minimum_steps_from_any_square())
