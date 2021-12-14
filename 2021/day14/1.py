def load():
    with open("input") as f:
        yield next(f).strip()
        next(f)
        for x in f:
            a, b = x.strip().split(" -> ")
            yield a, b


def pair_insertion():
    data = list(load())
    polymer, rules = list(data[0]), dict(data[1:])

    for _ in range(10):
        new_polymer = [polymer[0]]

        for i in range(len(polymer) - 1):
            pair = polymer[i] + polymer[i + 1]
            new_polymer.extend((rules[pair], polymer[i + 1]))

        polymer = new_polymer

    histogram = {}

    for e in polymer:
        histogram[e] = histogram.get(e, 0) + 1

    return max(histogram.values()) - min(histogram.values())


print(pair_insertion())
