def load():
    grid = {}
    with open("input") as f:
        for y, row in enumerate(f):
            for x, z in enumerate(row.strip()):
                grid[(x, y)] = z
    return grid


def is_visible(x, y, grid):
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        a, b = x, y
        while True:
            a, b = a + dx, b + dy
            c = grid.get((a, b))
            if c is None:
                return True
            elif c >= grid[(x, y)]:
                break
    return False


def count_visible_trees():
    grid = load()
    return sum(is_visible(x, y, grid) for x, y in grid)


print(count_visible_trees())
