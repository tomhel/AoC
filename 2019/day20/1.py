#!/usr/bin/env python3


import sys


sys.setrecursionlimit(10**6)


def load_input():
    maze = {}

    for y, row in enumerate(open("input")):
        for x, v in enumerate(list(row.strip("\n"))):
            maze[(x, y)] = v, (x, y)

    portals = {}

    for k, v in maze.items():
        x, y = k
        t, _ = v
        if t == ".":
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                a, b = x + dx, y + dy
                if ord("A") <= ord(maze.get((a, b), ("#", None))[0]) <= ord("Z"):
                    portal = maze[(a, b)][0] + maze[(a + dx, b + dy)][0]
                    portal = portal[::-1] if dx < 0 or dy < 0 else portal
                    maze[(x, y)] = "p", portal
                    portals[(x, y)] = portal
                    break

    for k, v in maze.items():
        x, y = k
        t, p = v
        if t == "p":
            dst = [k for k, v in portals.items() if v == p and k != (x, y)]
            maze[(x, y)] = ".", dst[0] if len(dst) > 0 else (x, y)

    maze["AA"] = [k for k, v in portals.items() if v == "AA"][0]
    maze["ZZ"] = [k for k, v in portals.items() if v == "ZZ"][0]

    return maze


def find_exit(pos, depth, maze, trace):
    x, y = pos
    paths = [float("inf")]

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        a, b = x + dx, y + dy
        if (a, b) == maze["ZZ"]:
            return depth + 1
        elif (a, b) in trace:
            continue

        v, p = maze.get((a, b), ("#", None))

        if v == ".":
            paths.append(find_exit(p, depth + (2 if (a, b) != p else 1), maze,
                                   trace + ([pos, (a, b)] if (a, b) != p else [pos])))

    return min(paths)


def solve_maze():
    maze = load_input()
    return find_exit(maze["AA"], 0, maze, [])


print(solve_maze())
