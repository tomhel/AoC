def load():
    with open("input") as f:
        for x in f:
            yield list(x.strip())


def determine_line_endings():
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<"
    }
    inv_pairs = {v: k for k, v in pairs.items()}

    for line in load():
        validator = []

        for char in line:
            if char in pairs.values():
                validator.append(char)
            elif validator.pop() != pairs[char]:
                validator = []
                break

        if len(validator) > 0:
            yield [inv_pairs[char] for char in reversed(validator)]


def calc_score():
    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }
    scores = []

    for ending in determine_line_endings():
        score = 0

        for char in ending:
            score = score * 5 + points[char]

        scores.append(score)

    return sorted(scores)[len(scores)//2]


print(calc_score())
