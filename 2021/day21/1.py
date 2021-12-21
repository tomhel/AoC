def load():
    with open("input") as f:
        for x in f:
            yield int(x.split(":")[1].strip())


def play():
    players = list(load())
    score = [0] * len(players)
    roll = 0

    while True:
        for p in range(len(players)):
            die = sum(x % 100 + 1 for x in range(roll, roll + 3))
            roll += 3
            pos = (players[p] + die - 1) % 10 + 1
            players[p] = pos
            score[p] += pos
            if score[p] >= 1000:
                return min(score) * roll


print(play())
