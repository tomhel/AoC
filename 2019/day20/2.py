#!/usr/bin/env python3


import sys
import math


sys.setrecursionlimit(10**6)


def load_input():
    maze = {}

    for y, row in enumerate(open("input")):
        for x, v in enumerate(list(row.strip("\n"))):
            maze[(x, y)] = v, (x, y), None

    portals = {}

    minx, miny = min(k for k, v in maze.items() if v[0] in ("#", "."))
    maxx, maxy = max(k for k, v in maze.items() if v[0] in ("#", "."))

    for k, v in maze.items():
        x, y = k
        t, _, _ = v
        if t == ".":
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                a, b = x + dx, y + dy
                if ord("A") <= ord(maze.get((a, b), ("#",))[0]) <= ord("Z"):
                    portal = maze[(a, b)][0] + maze[(a + dx, b + dy)][0]
                    portal = portal[::-1] if dx < 0 or dy < 0 else portal
                    maze[(x, y)] = "p", portal, None
                    portals[(x, y)] = portal, "INNER" if minx < x < maxx and miny < y < maxy else "OUTER"
                    break

    for k, v in maze.items():
        x, y = k
        t, p, _ = v
        if t == "p":
            dst = [k for k, v in portals.items() if v[0] == p and k != (x, y)]
            maze[(x, y)] = ".", dst[0] if len(dst) > 0 else (x, y), portals[dst[0]][1] if len(dst) > 0 else None

    maze["AA"] = [k for k, v in portals.items() if v[0] == "AA"][0]
    maze["ZZ"] = [k for k, v in portals.items() if v[0] == "ZZ"][0]

    return maze


def find_exit(pos, depth, maze, trace, best):
    x, y, z = pos

    if depth + 1 + z * 2 >= best[0]:
        return math.inf

    paths = [math.inf]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for i, delta in enumerate(directions):
        dx, dy = delta
        a, b = x + dx, y + dy

        if z > 0 and (a, b) in (maze["AA"], maze["ZZ"]):
            continue
        elif (a, b) == maze["ZZ"]:
            best[0] = min(best[0], depth + 1)
            return depth + 1
        elif (a, b, z) in trace:
            continue

        v, p, q = maze.get((a, b), ("#", None, None))
        px, py = p
        pz = z

        if v == ".":
            if p != (a, b):
                if q == "OUTER" and pz < 25:
                    if i < 3:
                        directions.append((dx, dy))
                        continue
                    pz += 1
                elif q == "INNER" and pz > 0:
                    pz -= 1
                else:
                    continue

            paths.append(find_exit((px, py, pz), depth + (2 if (a, b) != p else 1), maze,
                                   trace + ([pos, (a, b, z)] if (a, b) != p else [pos]), best))

    return min(paths)


def solve_maze():
    maze = load_input()
    pos = (maze["AA"][0], maze["AA"][1], 0)
    return find_exit(pos, 0, maze, [], [math.inf])


print(solve_maze())
