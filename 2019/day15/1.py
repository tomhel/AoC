#!/usr/bin/env python3


import intcode
import queue
import threading


def get_delta(direction):
    deltas = {
        1: (0, -1),
        2: (0, 1),
        3: (-1, 0),
        4: (1, 0)
    }
    return deltas[direction]


def get_inverse(direction):
    inverse = {
        1: 2,
        2: 1,
        3: 4,
        4: 3
    }
    return inverse[direction]


def find_oxygen_system(grid, pos, move_count, in_pipe, out_pipe):
    moves = [float("inf")]
    x, y = pos

    for direction in range(1, 5):
        dx, dy = get_delta(direction)
        a, b = x + dx, y + dy

        if (a, b) in grid:
            continue

        in_pipe.put(direction)
        response = out_pipe.get()
        grid[(a, b)] = response

        if response == 0:
            continue
        elif response == 1:
            moves.append(find_oxygen_system(grid, (a, b), move_count + 1, in_pipe, out_pipe))
        elif response == 2:
            return move_count + 1

        in_pipe.put(get_inverse(direction))
        out_pipe.get()

    return min(moves)


def run_robot():
    in_pipe = queue.Queue()
    out_pipe = queue.Queue()
    computer = intcode.Computer(intcode.load_program("input"), intcode.PipeIOHandler(in_pipe, out_pipe))
    t = threading.Thread(target=computer.execute)
    t.start()

    grid = {(0, 0): 1}
    moves = find_oxygen_system(grid, (0, 0), 0, in_pipe, out_pipe)

    computer.suspend()
    t.join()
    return moves


print(run_robot())
