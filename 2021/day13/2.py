import sys


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

    for axis, f in folds:
        if axis == "x":
            coords = {(x, y) for x, y in coords if x < f} | \
                     {(f - (x - f), y) for x, y in coords if x > f}
        elif axis == "y":
            coords = {(x, y) for x, y in coords if y < f} | \
                     {(x, f - (y - f)) for x, y in coords if y > f}

    return coords


def print_letters(coords):
    xlist, ylist = zip(*coords)

    for y in range(max(ylist) + 1):
        for x in range(max(xlist) + 1):
            print("#" if (x, y) in coords else " ", end="")
        print()


print_letters(fold())
