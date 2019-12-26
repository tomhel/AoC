#!/usr/bin/env python3


import math
import itertools


reachable_keys_cache = {}
maze_layout_cache = {}
keyring_scores = {}


def find_reachable_keys(pos, keyring, maze, depth, trace):
    x, y = pos
    paths = []

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        a, b = x + dx, y + dy
        if (a, b) in trace:
            continue

        square = maze.get((a, b), "#")

        if square in (".", "@"):
            paths.extend(find_reachable_keys((a, b), keyring, maze, depth + 1, trace + [pos]))
        elif ord("a") <= ord(square) <= ord("z"):
            if square in keyring:
                paths.extend(find_reachable_keys((a, b), keyring, maze, depth + 1, trace + [pos]))
            else:
                paths.append(((a, b), (square, depth + 1)))
                break
        elif ord("A") <= ord(square) <= ord("Z"):
            if square.lower() in keyring:
                paths.extend(find_reachable_keys((a, b), keyring, maze, depth + 1, trace + [pos]))

    return sorted(
        {(a[0], a[1]): c for a, c in sorted(paths, key=lambda i: i[1][1], reverse=True)}.items(),
        key=lambda i: i[1][1])


def unlock_vault(pos, keyring, maze, depth, all_keys, graph, best):
    cachekey = (pos, frozenset(keyring))
    score = keyring_scores.get(cachekey, math.inf)

    if score <= depth:
        return math.inf

    keyring_scores[cachekey] = depth
    reachable_keys = reachable_keys_cache.get(cachekey)

    if reachable_keys is None:
        reachable_keys = list(find_reachable_keys(pos, keyring, maze, 0, []))
        reachable_keys_cache[cachekey] = reachable_keys

    paths = [math.inf]

    for xpos, xkey in reachable_keys:
        a, b = xpos
        key, steps = xkey
        steps += depth

        if len(keyring) + 1 == len(all_keys):
            if steps < best[0]:
                print("current shortest path:", steps)
            best[0] = min(best[0], steps)
            return steps

        if steps + (len(all_keys) - len(keyring) - 1) >= best[0]:
            continue

        paths.append(unlock_vault((a, b), keyring + [key], simplify(maze, graph, keyring + ["@", key]),
                                  steps, all_keys, graph, best))

    return min(paths)


def find_shortest_path(pos, dst, maze, trace, best):
    x, y = pos
    u, v = dst
    du, dv = abs(x - u), abs(y - v)
    remain = math.sqrt(du**2 + dv**2)

    if dv != 0 and du != 0:
        remain /= math.sqrt(2)

    if len(trace) + math.ceil(remain) >= best[0]:
        return []

    paths = [[]]

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        a, b = x + dx, y + dy

        if (a, b) == dst:
            best[0] = min(best[0], len(trace) + 1)
            return trace + [pos, (a, b)]
        elif (a, b) in trace:
            continue

        square = maze.get((a, b), "#")

        if square == "#":
            continue
        else:
            paths.append(find_shortest_path((a, b), dst, maze, trace + [pos], best))

    return min(paths, key=lambda p: len(p) if len(p) > 0 else math.inf)


def simplify(maze, graph, keyring):
    ring = frozenset(keyring[:-1])
    cachekey = (frozenset(keyring[-1:]), ring)
    cached_maze = maze_layout_cache.get(cachekey)

    if cached_maze is not None:
        return cached_maze

    simplified_maze = {}

    for key, trace in graph.items():
        if key[0] in ring or key[1] in ring:
            continue

        if key[0] in keyring and key[1] in keyring:
            continue

        for x, y in trace:
            simplified_maze[(x, y)] = maze[(x, y)]

    maze_layout_cache[cachekey] = simplified_maze
    return simplified_maze


def get_shortest_key_paths(maze):
    keys = [(v, k) for k, v in maze.items() if ord("a") <= ord(v) <= ord("z")]
    entrance = [(v, k) for k, v in maze.items() if v == "@"]
    combos = list(itertools.combinations(keys + entrance, 2))
    graph = {}
    i = 0

    for a, b in combos:
        i += 1
        node1, pos1 = a
        node2, pos2 = b

        print("analyzing path [%s - %s] %d/%d" % (node1, node2, i, len(combos)))
        trace = find_shortest_path(pos1, pos2, maze, [], [math.inf])

        if len(trace) == 0:
            continue

        graph[(node1, node2)] = trace

    return graph


def load_input():
    maze = {}

    for y, row in enumerate(open("input")):
        for x, v in enumerate(list(row.strip())):
            maze[(x, y)] = v

    return maze


def solve_maze():
    maze = load_input()
    graph = get_shortest_key_paths(maze)
    maze = simplify(maze, graph, [])
    all_keys = [v for _, v in maze.items() if ord("a") <= ord(v) <= ord("z")]
    entrance = [k for k, v in maze.items() if v == "@"][0]
    return unlock_vault(entrance, [], maze, 0, all_keys, graph, [math.inf])


print(solve_maze())
