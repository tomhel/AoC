def load():
    board = {}
    with open("input") as f:
        for y, row in enumerate(f):
            for x, v in enumerate(row):
                if v == "\n":
                    continue
                board[(x+1, y+1)] = v
            if row.strip() == "":
                break
        return board, f.read().strip()


def next_move(path):
    n = ""
    for p in path:
        if p.isdigit():
            n += p
        else:
            yield int(n)
            n = ""
            yield p
    yield int(n)


def get_facing(turn, dx, dy):
    if turn == "L" and (dx, dy) in ((-1, 0), (1, 0)):
        return dy * -1, dx * -1
    elif turn == "L" and (dx, dy) in ((0, -1), (0, 1)):
        return dy, dx
    if turn == "R" and (dx, dy) in ((0, -1), (0, 1)):
        return dy * -1, dx * -1
    elif turn == "R" and (dx, dy) in ((-1, 0), (1, 0)):
        return dy, dx


def next_pos(x, y, dx, dy, board, maxx, maxy):
    if x < 1 or y < 1 or x > maxx or y > maxy:
        x = 1 if dx == 1 else x
        y = 1 if dy == 1 else y
        x = maxx if dx == -1 else x
        y = maxy if dy == -1 else y
        return next_pos(x, y, dx, dy, board, maxx, maxy)
    p = board.get((x, y), " ")
    if p == ".":
        return x, y
    elif p == "#":
        return None
    elif p == " ":
        return next_pos(x + dx, y + dy, dx, dy, board, maxx, maxy)


def follow_path(board, path):
    y, x = min((y, x) for x, y in board if board[(x, y)] == ".")
    maxx, maxy = max(x for x, _ in board), max(y for _, y in board)
    dx, dy = 1, 0
    for m in next_move(path):
        if m in ("L", "R"):
            dx, dy = get_facing(m, dx, dy)
        else:
            for _ in range(m):
                p = next_pos(x + dx, y + dy, dx, dy, board, maxx, maxy)
                if p is None:
                    break
                x, y = p
    return x, y, dx, dy


def final_password():
    board, path = load()
    x, y, dx, dy = follow_path(board, path)
    f = {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}[(dx, dy)]
    return 1000 * y + 4 * x + f


print(final_password())
