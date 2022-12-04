def load():
    with open("input") as f:
        for x in f:
            r1, r2 = x.strip().split(",")
            yield map(int, r1.split("-") + r2.split("-"))


def find_fully_contained():
    return sum((a <= x and b >= y) or (x <= a and y >= b) for a, b, x, y in load())


print(find_fully_contained())
