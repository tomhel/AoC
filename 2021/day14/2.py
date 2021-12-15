def load():
    with open("input") as f:
        yield next(f).strip()
        next(f)
        for x in f:
            yield x.strip().split(" -> ")


def pair_insertion():
    data = list(load())
    template, rules = data[0], dict(data[1:])
    polymer = {}

    for i in range(len(template) - 1):
        pair = template[i] + template[i+1]
        polymer[pair] = polymer.get(pair, 0) + 1

    for _ in range(40):
        new_polymer = {}

        for pair in polymer:
            e = rules[pair]
            pair1, pair2 = pair[0] + e, e + pair[1]
            new_polymer[pair1] = new_polymer.get(pair1, 0) + polymer[pair]
            new_polymer[pair2] = new_polymer.get(pair2, 0) + polymer[pair]

        polymer = new_polymer

    histogram = {template[0]: 1}

    for pair in polymer:
        histogram[pair[1]] = histogram.get(pair[1], 0) + polymer[pair]

    return max(histogram.values()) - min(histogram.values())


print(pair_insertion())
