#!/usr/bin/env python3


import intcode


def run_game():
    grid = {}
    computer = intcode.Computer(intcode.load_program("input"), intcode.BufferIOHandler())
    computer.execute()
    grid_data = computer.get_output()

    for x, y, tile_id in (grid_data[i:i+3] for i in range(0, len(grid_data), 3)):
        grid[(x, y)] = tile_id

    return sum(1 for v in grid.values() if v == 2)


print(run_game())
