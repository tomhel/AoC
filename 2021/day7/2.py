def load():
    with open("input") as f:
        return [int(x) for x in f.read().strip().split(",")]


def align_crabs():
    crabs = load()
    min_fuel = None

    for pos in range(min(crabs), max(crabs) + 1):
        fuel = sum((abs(c - pos) * (abs(c - pos) + 1)) // 2 for c in crabs)
        min_fuel = fuel if min_fuel is None else min(min_fuel, fuel)

    return min_fuel


print(align_crabs())
