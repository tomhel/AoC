def load():
    with open("input") as f:
        for x in f:
            yield x.strip()


def to_decimal(binary):
    return int(binary, 2)


def calc_oxygen_rating():
    keep = list(load())

    for i in range(len(keep[0])):
        ones = sum(x[i] == "1" for x in keep)
        bit = "1" if len(keep) - ones <= ones else "0"
        keep = [x for x in keep if x[i] == bit]
        if len(keep) == 1:
            return to_decimal(keep.pop())


def calc_co2_rating():
    keep = list(load())

    for i in range(len(keep[0])):
        ones = sum(x[i] == "1" for x in keep)
        bit = "1" if len(keep) - ones > ones else "0"
        keep = [x for x in keep if x[i] == bit]
        if len(keep) == 1:
            return to_decimal(keep.pop())


print(calc_oxygen_rating() * calc_co2_rating())
