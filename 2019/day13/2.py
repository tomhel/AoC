#!/usr/bin/env python3
#
# Must run in terminal for animations to work.
# Tested on Linux.


import intcode
import queue
import threading
import sys


def put_text(x, y, text):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (y, x, text))
    sys.stdout.flush()


def draw_screen(out_pipe, com):
    sys.stdout.write(chr(27) + "[2J")
    sys.stdout.flush()

    chars = {
        0: " ", 1: "*", 2: "@", 3: "=", 4: "o"
    }

    while True:
        x = out_pipe.get()
        if x is None:
            break

        y = out_pipe.get()
        if y is None:
            break

        tile_id = out_pipe.get()
        if tile_id is None:
            break

        if (x, y) == (-1, 0):
            put_text(2, 2, "score: %d" % tile_id)
            continue
        elif tile_id in (3, 4):
            com.put((tile_id, x, y))

        put_text(x + 2, y + 3, chars[tile_id])

    com.put(None)


def control_joystick(in_pipe, com):
    tiles = {
        3: None, 4: None
    }

    while True:
        try:
            while True:
                t = com.get(timeout=0.01)
                if t is None:
                    return
                tiles[t[0]] = (t[1], t[2])
        except queue.Empty:
            pass

        if tiles[3] is None or tiles[4] is None:
            in_pipe.put(0)
            continue

        paddle, ball = tiles[3], tiles[4]
        dx = (ball[0] - paddle[0]) // max(abs(ball[0] - paddle[0]), 1)
        in_pipe.put(dx)


def run_game():
    in_pipe = queue.Queue()
    out_pipe = queue.Queue()
    com = queue.Queue()

    program = intcode.load_program("input")
    program[0] = 2
    computer = intcode.Computer(program, intcode.PipeIOHandler(in_pipe, out_pipe))

    computer_thread = threading.Thread(target=computer.execute)
    draw_thread = threading.Thread(target=draw_screen, args=(out_pipe, com))
    joystick_thread = threading.Thread(target=control_joystick, args=(in_pipe, com))

    computer_thread.start()
    draw_thread.start()
    joystick_thread.start()

    computer_thread.join()
    draw_thread.join()
    joystick_thread.join()


run_game()
