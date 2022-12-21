def load():
    with open("input") as f:
        for n in f:
            yield int(n.strip())


def mix(numbers):
    lookup = [i for i, _ in enumerate(numbers)]
    length = len(numbers)
    for i in range(length):
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


def find_grove_coordinates():
    numbers = mix(list(load()))
    return sum(numbers[(i + numbers.index(0)) % len(numbers)] for i in (1000, 2000, 3000))


print(find_grove_coordinates())
