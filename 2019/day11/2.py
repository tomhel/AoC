#!/usr/bin/env python3


import intcode
import queue
import threading


def move(current_dir, turn):
    if current_dir == "U":
        return ("L", -1, 0) if turn == 0 else ("R", 1, 0)
    elif current_dir == "D":
        return ("R", 1, 0) if turn == 0 else ("L", -1, 0)
    elif current_dir == "L":
        return ("D", 0, 1) if turn == 0 else ("U", 0, -1)
    elif current_dir == "R":
        return ("U", 0, -1) if turn == 0 else ("D", 0, 1)


def run_robot():
    grid = {}
    direction, x, y = "U", 0, 0

    in_pipe = queue.Queue()
    out_pipe = queue.Queue()
    io_handler = intcode.PipeIOHandler(in_pipe, out_pipe)

    computer = intcode.Computer(intcode.load_program("input"), io_handler)
    t = threading.Thread(target=computer.execute)
    t.start()
    i = 0

    while t.is_alive():
        color = grid.get((x, y), 1 if i == 0 else 0)
        in_pipe.put(color)
        new_color = out_pipe.get()
        if new_color is None:
            break
        turn = out_pipe.get()
        if turn is None:
            break
        grid[(x, y)] = new_color
        direction, dx, dy = move(direction, turn)
        x, y = x + dx, y + dy
        i += 1

    return grid


def render_grid(grid):
    minx, miny = min(x for x, _ in grid), min(y for _, y in grid)
    maxx, maxy = max(x for x, _ in grid), max(y for _, y in grid)

    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            print(" " if grid.get((x, y), 0) == 0 else "@", end="")
        print()


render_grid(run_robot())
