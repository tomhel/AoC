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

    while t.is_alive():
        color = grid.get((x, y), 0)
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

    return grid


print(len(run_robot()))
