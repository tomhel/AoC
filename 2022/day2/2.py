def load():
    with open("input") as f:
        for x in f:
            yield x.strip().split()


def get_score(s1, s2):
    scores = {"A": 1, "B": 2, "C": 3}
    beats = {"A": "C", "B": "A", "C": "B"}
    if s1 == s2:
        return scores[s1] + 3
    elif s2 == beats[s1]:
        return scores[s1] + 6
    else:
        return scores[s1]


def select(shp, strategy):
    beats = {"A": "C", "B": "A", "C": "B"}
    if strategy == "X":  # lose
        return beats[shp]
    elif strategy == "Y":  # draw
        return shp
    elif strategy == "Z":  # win
        return {v: k for k, v in beats.items()}[shp]


def calc_score():
    return sum(get_score(select(s1, s2), s1) for s1, s2 in load())


print(calc_score())
