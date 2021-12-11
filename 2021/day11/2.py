def load():
    with open("input") as f:
        grid = {}

        for y, row in enumerate(f):
            grid.update({(x, y): int(v) for x, v in enumerate(row.strip())})

        return grid


def flash(pos, flashed, grid):
    if pos in flashed or pos not in grid:
        return

    flashed.add(pos)
    grid[pos] = 0
    x, y = pos

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i, j) in flashed or (i, j) not in grid:
                continue

            grid[(i, j)] += 1

            if grid[(i, j)] > 9:
                flash((i, j), flashed, grid)


def simulate():
    grid = load()
    step = 0

    while True:
        step += 1

        for pos in grid:
            grid[pos] += 1

        flashed = set()

        for pos in grid:
            if grid[pos] > 9:
                flash(pos, flashed, grid)

        if len(flashed) == len(grid):
            return step


print(simulate())
