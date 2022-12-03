def load():
    with open("input") as f:
        for x in f:
            yield x.strip()


def get_prio(items):
    return sum(ord(x) - ord("a") + 1 if x == x.lower() else ord(x) - ord("A") + 27 for x in items)


def sum_prio_items():
    sacks = list(load())
    return sum(get_prio(set(sacks[i]) & set(sacks[i+1]) & set(sacks[i+2])) for i in range(0, len(sacks), 3))


print(sum_prio_items())
