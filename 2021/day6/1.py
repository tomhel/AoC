def load():
    with open("input") as f:
        return [int(i) for i in f.read().strip().split(",")]


def simulate(days):
    fish = load()

    for _ in range(days):
        for i in range(len(fish)):
            if fish[i] == 0:
                fish[i] = 6
                fish.append(8)
            else:
                fish[i] -= 1

    return len(fish)


print(simulate(80))
