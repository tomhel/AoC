def load():
    with open("input") as f:
        for x in f:
            p1, p2 = x.strip().split(" -> ")
            yield [int(x) for x in p1.split(",")] + [int(x) for x in p2.split(",")]


def num_overlaps():
    grid = {}

    for x1, y1, x2, y2 in load():
        if x1 != x2 and y2 != y1:
            continue

        dx = (x2 - x1) // abs(x2 - x1) if x2 - x1 != 0 else 0
        dy = (y2 - y1) // abs(y2 - y1) if y2 - y1 != 0 else 0
        x, y = x1, y1

        while True:
            n = grid.get((x, y), 0)
            grid[(x, y)] = n + 1
            if x == x2 and y == y2:
                break
            x, y = x + dx, y + dy

    return sum(1 for n in grid.values() if n >= 2)


print(num_overlaps())
