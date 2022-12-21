def load():
    with open("input") as f:
        for n in f:
            yield int(n.strip())


def mix(numbers):
    lookup = [i for i, _ in enumerate(numbers)]
    length = len(numbers)
    for i in range(length * 10):
        a = i % length
        n = numbers[lookup[a]]
        b = (lookup[a] + n) % (length - 1)
        numbers.insert(b, numbers.pop(lookup[a]))
        for x in range(length):
            if lookup[a] < lookup[x]:
                lookup[x] -= 1
        for x in range(length):
            if lookup[x] >= b:
                lookup[x] += 1
        lookup[a] = b
    return numbers


def apply_decryption_key(numbers):
    key = 811589153
    return [n * key for n in numbers]


def find_grove_coordinates():
    numbers = mix(apply_decryption_key(load()))
    return sum(numbers[(i + numbers.index(0)) % len(numbers)] for i in (1000, 2000, 3000))


# takes about 3 seconds to run using PyPy. 30 seconds using CPython.
print(find_grove_coordinates())
