import re


def load():
    maze = {}
    with open("input") as f:
        for row in f:
            m = re.match(r"^Valve\s(..).*rate=(\d+);.*valves?\s(.+)$", row)
            maze[m.group(1)] = (int(m.group(2)), m.group(3).split(", "))
    return maze


def estimate_max_pressure(opened, pressure, t, maze):
    valves = sorted((v for v in maze if v not in opened), key=lambda k: maze[k][0],  reverse=True)
    for i in range(30 - t):
        last_opened = None
        if i < len(valves):
            opened.add(valves[i])
            last_opened = valves[i]
        pressure += sum(maze[v][0] for v in opened if v != last_opened)
    return pressure


def find_path(valve, opened, pressure, t, visited, maze, best):
    all_opened = len(opened) == len([v for v in maze if maze[v][0] > 0])
    p = sum(maze[v][0] for v in opened)
    if t > 30 or all_opened:
        pressure += p * (31 - t)
        best[0] = max(pressure, best[0])
        return pressure
    pressure += p
    if estimate_max_pressure(set(opened), pressure, t, maze) <= best[0]:
        return 0
    score = [0]
    for v in maze[valve][1]:
        if maze[valve][0] > 0 and valve not in opened:
            score.append(find_path(v, opened | {valve}, pressure + p, t+2, {valve}, maze, best))
        if v not in visited:
            score.append(find_path(v, set(opened), pressure, t+1, visited | {valve}, maze, best))
    return max(score)


def maximum_pressure_release():
    return find_path("AA", set(), 0, 0, set(), load(), [0])


# takes about 30 seconds to run
print(maximum_pressure_release())
