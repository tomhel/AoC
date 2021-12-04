def load():
    with open("input") as f:
        yield [int(x) for x in next(f).strip().split(",")]
        board, row = {}, 0

        for x in f:
            if len(x.strip()) == 0:
                if len(board) > 0:
                    yield board
                board, row = {}, 0
                continue

            x = [int(n) for n in x.strip().split(" ") if n != ""]
            board.update({n: (i, row) for i, n in enumerate(x)})
            row += 1

        if len(board) > 0:
            yield board


def update_stat(pos, stat):
    x, y = pos
    score_x = stat.get(f"x{x}", 0) + 1
    score_y = stat.get(f"y{y}", 0) + 1
    stat[f"x{x}"] = score_x
    stat[f"y{y}"] = score_y


def bingo(stat):
    for v in stat.values():
        if v >= 5:
            return True

    return False


def find_winning_board():
    data = list(load())
    numbers = data[0]
    boards = data[1:]
    stats = [{} for _ in range(len(boards))]

    for i, n in enumerate(numbers):
        for b, board in enumerate(boards):
            pos = board.get(n)
            if pos is None:
                continue
            update_stat(pos, stats[b])
            if bingo(stats[b]):
                return board, numbers[:i+1]


def calc_score():
    board, numbers = find_winning_board()
    return sum(n for n in board if n not in numbers) * numbers[-1]


print(calc_score())
