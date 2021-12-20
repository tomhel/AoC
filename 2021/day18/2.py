from itertools import permutations
import copy
import json


class Number:
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return str(self.n)


def load():
    with open("input") as f:
        for x in f:
            yield json.loads(x, parse_int=lambda i: Number(int(i)))


def explode(num, flat, depth=0):
    if depth > 3:
        a, b = num
        idx_a, idx_b = flat.index(a), flat.index(b)
        if idx_a - 1 >= 0:
            flat[idx_a - 1].n += a.n
        if idx_b + 1 < len(flat):
            flat[idx_b + 1].n += b.n
        a.n = 0
        flat.pop(idx_b)
    else:
        for i in range(2):
            if isinstance(num[i], list):
                explode(num[i], flat, depth + 1)
                if depth == 3:
                    num[i] = num[i][0]


def flatten(num):
    if isinstance(num, Number):
        return [num]
    else:
        return sum((flatten(n) for n in num), [])


def split(num):
    if isinstance(num, Number):
        return (num, False) if num.n <= 9 else ([Number(num.n // 2), Number(num.n // 2 + num.n % 2)], True)

    num[0], changed = split(num[0])
    if not changed:
        num[1], changed = split(num[1])
    return num, changed


def reduce(num):
    changed = True

    while changed:
        explode(num, flatten(num))
        _, changed = split(num)

    return num


def magnitude(num):
    if isinstance(num, Number):
        return num.n
    elif isinstance(num, list) and isinstance(num[0], Number) and isinstance(num[1], Number):
        return 3 * num[0].n + 2 * num[1].n
    else:
        return 3 * magnitude(num[0]) + 2 * magnitude(num[1])


def add(a, b):
    return [copy.deepcopy(a), copy.deepcopy(b)]


def calculate_largest_magnitude():
    numbers = list(load())
    return max(magnitude(reduce(add(a, b))) for a, b in permutations(numbers, 2))


print(calculate_largest_magnitude())
