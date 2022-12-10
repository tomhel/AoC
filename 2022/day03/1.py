def load():
    with open("input") as f:
        for x in map(lambda k: k.strip(), f):
            yield x[:len(x)//2], x[len(x)//2:]


def get_prio(items):
    return sum(ord(x) - ord("a") + 1 if x == x.lower() else ord(x) - ord("A") + 27 for x in items)


def sum_prio_items():
    return sum(get_prio(set(c1) & set(c2)) for c1, c2 in load())


print(sum_prio_items())
