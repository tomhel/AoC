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
            if (i, j) in grid and (i, j) not in flashed:
                grid[(i, j)] += 1

                if grid[(i, j)] > 9:
                    flash((i, j), flashed, grid)


def simulate(steps):
    grid = load()
    count = 0

    for _ in range(steps):
        for pos in grid:
            grid[pos] += 1

        flashed = set()

        for pos in grid:
            if grid[pos] > 9:
                flash(pos, flashed, grid)

        count += len(flashed)

    return count


print(simulate(100))
