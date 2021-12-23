def load():
    with open("input") as f:
        for x in f:
            yield int(x.split(":")[1].strip())


def roll(players, p, score, wins, universes):
    # Go through all possible sums of three die throws, and how many ways to get them.
    # For example, there is 1 way to get a sum of 3 (1, 1, 1). 3 ways to get a sum of 4 and so on...
    for die, count in [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]:
        score2 = list(score)
        players2 = list(players)
        pos = (players2[p] + die - 1) % 10 + 1
        players2[p] = pos
        score2[p] += pos

        if score2[p] >= 21:
            wins[p] += universes * count
        else:
            roll(players2, (p + 1) % 2, score2, wins, universes * count)

    return wins


def play():
    players = list(load())
    return max(roll(players, 0, [0] * len(players), [0] * len(players), 1))


# Takes about 1 minute to run...
print(play())
