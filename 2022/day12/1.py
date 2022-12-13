def load():
    heightmap = {}
    with open("input") as f:
        for y, row in enumerate(x.strip() for x in f):
            for x, z in enumerate(row):
                heightmap[(x, y)] = z
        return heightmap


def find_path(start, goal, heightmap):
    q, visited = [(start, 0)], set()
    while len(q) > 0:
        pos, steps = q.pop(0)
        if pos in visited:
            continue
        visited.add(pos)
        if heightmap[pos] == goal:
            return steps
        for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
            a, b = pos[0] + dx, pos[1] + dy
            square = heightmap.get((a, b))
            square = "z" if square == "E" else square
            if square and ord(square) - 1 <= ord("a" if heightmap[pos] == "S" else heightmap[pos]):
                q.append(((a, b), steps + 1))


def minimum_steps():
    heightmap = load()
    start = [k for k, v in heightmap.items() if v == "S"][0]
    return find_path(start, "E", heightmap)


print(minimum_steps())
