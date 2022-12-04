def load():
    with open("input") as f:
        for x in f:
            r1, r2 = x.strip().split(",")
            yield map(int, r1.split("-") + r2.split("-"))


def find_fully_contained():
    return sum((x <= a <= y) or (x <= b <= y) or (a <= x <= b) or (a <= y <= b) for a, b, x, y in load())


print(find_fully_contained())
