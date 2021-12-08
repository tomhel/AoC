def load():
    with open("input") as f:
        for x in f:
            a, b, = x.strip().split("|")
            yield a.strip().split(), b.strip().split()


def num_unique_segments():
    count = 0

    for _, out in load():
        count += sum(1 for x in out if len(x) in (2, 3, 4, 7))

    return count


print(num_unique_segments())
