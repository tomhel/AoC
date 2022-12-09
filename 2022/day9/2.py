def load():
    with open("input") as f:
        for line in f:
            a, b = line.strip().split(" ")
            yield a, int(b)


def get_direction(move):
    if move == "L":
        return -1, 0
    elif move == "R":
        return 1, 0
    elif move == "U":
        return 0, 1
    elif move == "D":
        return 0, -1


def is_touching(head, tail):
    x, y = head
    a, b = tail
    return (x == a and abs(y - b) <= 1) or (y == b and abs(x - a) <= 1) or (abs(x - a) <= 1 and abs(y - b) <= 1)


def get_move(head, tail):
    x, y = head
    a, b = tail
    return (0 if x - a == 0 else (x - a) // abs(x - a)), (0 if y - b == 0 else (y - b) // abs(y - b))


def simulate_motions():
    rope = [(0, 0)] * 10
    visited = {(0, 0)}
    for move, steps in load():
        dx, dy = get_direction(move)
        for _ in range(steps):
            rope[0] = rope[0][0] + dx, rope[0][1] + dy
            for i in range(1, len(rope)):
                if not is_touching(rope[i-1], rope[i]):
                    dxx, dyy = get_move(rope[i-1], rope[i])
                    rope[i] = rope[i][0] + dxx, rope[i][1] + dyy
                    if i == len(rope) - 1:
                        visited.add(rope[i])
    return len(visited)


print(simulate_motions())
