def load():
    with open("input") as f:
        for x in f:
            yield x.strip().split()


def get_score(s1, s2):
    mapping = {"A": "X", "B": "Y", "C": "Z"}
    scores = {"X": 1, "Y": 2, "Z": 3}
    beats = {"X": "C", "Y": "A", "Z": "B"}
    if s1 == mapping[s2]:
        return scores[s1] + 3
    elif s2 == beats[s1]:
        return scores[s1] + 6
    else:
        return scores[s1]


def calc_score():
    return sum(get_score(s2, s1) for s1, s2 in load())


print(calc_score())
