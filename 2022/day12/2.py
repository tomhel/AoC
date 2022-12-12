import math
import sys


def load():
    heightmap = {}
    with open("input") as f:
        for y, row in enumerate(x.strip() for x in f):
            for x, z in enumerate(row):
                heightmap[(x, y)] = z
        return heightmap


def find_path(pos, heightmap, best, visited, goal, highscore):
    if len(visited) >= highscore:
        return math.inf  # shorter path already found to another a-node.
    if highscore <= len(visited) + abs(pos[0] - goal[0]) + abs(pos[1] - goal[1]):
        return math.inf  # current path will not lead to a shorter a-node path (manhattan distance).
    visited.add(pos)
    if best.get(pos, math.inf) <= len(visited):
        return math.inf  # shorter path already found to this node.
    if best.get(goal, math.inf) <= len(visited) + abs(pos[0] - goal[0]) + abs(pos[1] - goal[1]):
        return math.inf  # current path will not lead to a shorter path to goal (manhattan distance).
    if pos == goal:
        return len(visited) - 1
    if heightmap[pos] == "a":
        return math.inf  # no need to continue if an a-node is in the path.
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
            steps.append(find_path((a, b), heightmap, best, set(visited), goal, highscore))
    return min(steps)


def minimum_steps_from_any_square():
    sys.setrecursionlimit(10**6)
    heightmap = load()
    goal = [k for k, v in heightmap.items() if v == "E"][0]
    start = [k for k, v in heightmap.items() if v == "S"][0]
    min_steps = math.inf
    for x, y in [start] + [k for k, v in heightmap.items() if v == "a"]:
        if "b" in [heightmap.get((x + dx, y + dy)) for dx, dy in [(-1, 0), (0, 1), (0, -1), (1, 0)]]:
            # if a-node does not have a b-node neighbour, do not even consider it.
            steps = find_path(goal, heightmap, {}, set(), (x, y), min_steps)
            min_steps = min(steps, min_steps)
    return min_steps


# takes about 80 seconds to run.
print(minimum_steps_from_any_square())
