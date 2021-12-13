def load():
    with open("input") as f:
        coords, folds = set(), []

        for x in f:
            if x.startswith("fold"):
                a, b = x.strip().split()[-1].split("=")
                folds.append((a, int(b)))
            elif len(x.strip()) != 0:
                a, b = x.strip().split(",")
                coords.add((int(a), int(b)))

        return coords, folds


def fold():
    coords, folds = load()
    axis, f = folds[0]

    if axis == "x":
        coords = {(x, y) for x, y in coords if x < f} | \
                 {(f - (x - f), y) for x, y in coords if x > f}
    elif axis == "y":
        coords = {(x, y) for x, y in coords if y < f} | \
                 {(x, f - (y - f)) for x, y in coords if y > f}

    return len(coords)


print(fold())
