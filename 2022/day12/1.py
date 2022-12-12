import math
import sys


def load():
    heightmap = {}
    with open("input") as f:
        for y, row in enumerate(x.strip() for x in f):
            for x, z in enumerate(row):
                heightmap[(x, y)] = z
        return heightmap


def find_path(pos, heightmap, best, visited, goal):
    visited.add(pos)
    if best.get(pos, math.inf) <= len(visited):
        return math.inf  # shorter path already found to this node.
    if best.get(goal, math.inf) <= len(visited) + abs(pos[0] - goal[0]) + abs(pos[1] - goal[1]):
        return math.inf  # current path will not lead to a shorter path to goal (manhattan distance).
    if pos == goal:
        return len(visited) - 1
    best[pos] = len(visited)
    steps = [math.inf]
    current = heightmap[pos]
    for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        a, b = pos[0] + dx, pos[1] + dy
        square = heightmap.get((a, b))
        square = "z" if square == "E" else square
        if square is None or (a, b) in visited:
            continue
        elif ord(square) - 1 <= ord("a" if current == "S" else current):
            steps.append(find_path((a, b), heightmap, best, set(visited), goal))
    return min(steps)


def minimum_steps():
    sys.setrecursionlimit(10**6)
    heightmap = load()
    start = [k for k, v in heightmap.items() if v == "S"][0]
    goal = [k for k, v in heightmap.items() if v == "E"][0]
    return find_path(start, heightmap, {}, set(), goal)


# takes about 30 seconds to run.
print(minimum_steps())
