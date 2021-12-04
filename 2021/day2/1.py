def load():
    with open("input") as f:
        for x in f:
            x = x.strip().split(" ")
            yield x[0], int(x[1])


def calculate_position():
    horizontal = 0
    depth = 0

    for cmd, units in load():
        if cmd == "forward":
            horizontal += units
        elif cmd == "up":
            depth -= units
        elif cmd == "down":
            depth += units
        else:
            raise Exception(f"unknown command: {cmd}")

    return horizontal * depth


print(calculate_position())
