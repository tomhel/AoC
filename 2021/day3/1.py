def load():
    with open("input") as f:
        for x in f:
            yield x.strip()


def to_decimal(binary):
    return int(binary, 2)


def calculate_power_consumption():
    report = list(load())
    ones = []

    for i in range(len(report[0])):
        ones.append(sum(int(x[i]) for x in report))

    gamma = "".join(str(int(x > len(report) - x)) for x in ones)
    epsilon = "".join(str(int(x <= len(report) - x)) for x in ones)

    return to_decimal(gamma) * to_decimal(epsilon)


print(calculate_power_consumption())
