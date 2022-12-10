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
    head, tail = (0, 0), (0, 0)
    visited = {(0, 0)}
    for move, steps in load():
        dx, dy = get_direction(move)
        for _ in range(steps):
            head = head[0] + dx, head[1] + dy
            if not is_touching(head, tail):
                dxx, dyy = get_move(head, tail)
                tail = tail[0] + dxx, tail[1] + dyy
                visited.add(tail)
    return len(visited)


print(simulate_motions())
