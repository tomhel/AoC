def load():
    with open("input") as f:
        for x in f:
            yield int(x.split(":")[1].strip())


def play():
    players = list(load())
    score = [0] * len(players)
    die = 0

    while True:
        for p in range(len(players)):
            moves = sum(x % 100 + 1 for x in range(die, die + 3))
            die += 3
            pos = (players[p] + moves - 1) % 10 + 1
            players[p] = pos
            score[p] += pos
            if score[p] >= 1000:
                return min(score) * die


print(play())
