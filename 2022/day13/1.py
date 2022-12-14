import json


def load():
    with open("input") as f:
        packet = []
        for row in f:
            if row.strip() == "":
                yield packet
                packet = []
                continue
            packet.append(json.loads(row))
        yield packet


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, list) and isinstance(right, list):
        i = 0
        while True:
            if i >= len(left) or i >= len(right):
                return len(left) - len(right)
            res = compare(left[i], right[i])
            if res != 0:
                return res
            i += 1


def sum_indices_of_correct_order():
    return sum(i + 1 for i, pkt in enumerate(load()) if compare(pkt[0], pkt[1]) <= 0)


print(sum_indices_of_correct_order())
