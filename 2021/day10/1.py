def load():
    with open("input") as f:
        for x in f:
            yield list(x.strip())


def find_corruptions():
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<"
    }
    for line in load():
        validator = []
        for char in line:
            if char in pairs.values():
                validator.append(char)
            elif validator.pop() != pairs[char]:
                yield char
                break


def calc_score():
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    return sum(points[char] for char in find_corruptions())


print(calc_score())
