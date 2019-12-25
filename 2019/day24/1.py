#!/usr/bin/env python3


def load_input():
    grid = {}

    for y, row in enumerate(open("input")):
        for x, v in enumerate(list(row.strip())):
            grid[(x, y)] = v

    return grid


def adjacent_bugs(x, y, grid):
    count = 0

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if grid.get((x + dx, y + dy), ".") == "#":
            count += 1

    return count


def get_biodiversity_rating():
    grid = load_input()
    ratings = set()

    while True:
        new_grid = {}

        for p, t in grid.items():
            x, y = p

            if t == "#":
                new_grid[(x, y)] = "#" if adjacent_bugs(x, y, grid) == 1 else "."
            else:
                new_grid[(x, y)] = "#" if adjacent_bugs(x, y, grid) in (1, 2) else "."

        grid = new_grid
        rating = 0

        for i, p in enumerate(sorted(grid, key=lambda k: (k[1], k[0]))):
            if grid[p] == "#":
                rating += 2**i

        if rating in ratings:
            return rating
        else:
            ratings.add(rating)


print(get_biodiversity_rating())
