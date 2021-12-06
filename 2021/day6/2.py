def load():
    with open("input") as f:
        return [int(i) for i in f.read().strip().split(",")]


def simulate(days):
    fish = [0] * 9

    for t in load():
        fish[t] += 1

    for _ in range(days):
        n = fish.pop(0)
        fish[6] += n
        fish.append(n)

    return sum(n for n in fish)


print(simulate(256))
