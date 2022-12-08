def load():
    grid = {}
    with open("input") as f:
        for y, row in enumerate(f):
            for x, z in enumerate(row.strip()):
                grid[(x, y)] = z
    return grid


def get_score(x, y, grid):
    z, score = grid[(x, y)], 1
    for i, pos in enumerate([(1, 0), (0, 1), (-1, 0), (0, -1)]):
        dx, dy = pos
        a, b, s = x, y, 0
        while True:
            a, b = a + dx, b + dy
            c = grid.get((a, b))
            if c is None:
                break
            elif c < z:
                s += 1
            elif c >= z:
                s += 1
                break
        score *= s
    return score


def find_highest_scenic_score():
    grid = load()
    return max(get_score(x, y, grid) for x, y in grid)


print(find_highest_scenic_score())
