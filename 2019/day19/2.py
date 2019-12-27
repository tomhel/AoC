#!/usr/bin/env python3


import intcode


prog = intcode.load_program("input")
measurement_cache = {}


def deploy_drone(x, y):
    r = measurement_cache.get((x, y))

    if r is not None:
        return r

    computer = intcode.Computer(prog[:], intcode.BufferIOHandler([x, y]))
    computer.execute()
    r = computer.get_output()[0]
    measurement_cache[(x, y)] = r
    return r


def analyze_beam():
    santa_w, santa_h = 100, 100
    y, xmin = 0, 0

    while True:
        x, w = xmin, 0

        while True:
            if deploy_drone(x, y) == 1:
                if w == 0:
                    xmin = x
                w += 1
            elif w > 0:
                break
            elif x > (xmin + 1) * 2:
                break

            x += 1

        y += 1

        if w < santa_w:
            continue

        for xx in range(x - w, x + 1 - santa_w):
            yy, h = y - 1, 0

            while True:
                if deploy_drone(xx, yy) == 1:
                    h += 1
                else:
                    break

                yy += 1

            if h >= santa_h:
                return xx * 10000 + yy - h


print(analyze_beam())
