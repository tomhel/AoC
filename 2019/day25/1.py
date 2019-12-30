#!/usr/bin/env python3


import intcode
import queue
import threading
import itertools


excluded_items = {
    "giant electromagnet",
    "molten lava",
    "infinite loop",
    "escape pod",
    "photons"
}

directions = {
    "east": "west",
    "west": "east",
    "south": "north",
    "north": "south"
}

security_checkpoint = "Security Checkpoint"


def play(computer):
    room = None
    doors = []
    items = []

    while True:
        text = computer.get_decoded_output()

        if text is None:
            return room, doors, items

        print(text)

        if text == "Command?":
            return room, doors, items

        if text.startswith("== "):
            room = text.strip("= ")
        elif text.startswith("- "):
            x = text.strip("- ")
            if x in directions:
                doors.append(x)
            else:
                items.append(x)


def explore(computer, trace):
    room, doors, items = play(computer)

    if room in trace:
        return []

    trace.append(room)
    moves = []

    for item in items:
        if item in excluded_items:
            continue

        command("take " + item, computer)
        play(computer)

    if room == security_checkpoint:
        doors.remove("north")

    for door in doors:
        moves.append((room, door))
        command(door, computer)
        moves.extend(explore(computer, trace))
        moves.append((room, directions[door]))
        command(directions[door], computer)
        play(computer)

    return moves


def command(cmd, computer):
    print(">>> " + cmd)
    computer.input_text(cmd + "\n")


def goto(room, moves, computer):
    for r, m in moves:
        if r == room:
            return

        command(m, computer)
        play(computer)


def spoof_identity(computer):
    command("inv", computer)
    _, _, items = play(computer)

    for item in items:
        command("drop " + item, computer)
        play(computer)

    item_combos = sum([list(itertools.combinations(items, i)) for i in range(1, len(items) + 1)], [])

    for combo in item_combos:
        for item in combo:
            command("take " + item, computer)
            play(computer)

        command("north", computer)
        room, _, _ = play(computer)

        if room != security_checkpoint:
            return

        for item in combo:
            command("drop " + item, computer)
            play(computer)


def deploy_droid():
    computer = intcode.Computer(intcode.load_program("input"), intcode.PipeIOHandler(queue.Queue(), queue.Queue()))
    t = threading.Thread(target=computer.execute)
    t.start()

    moves = explore(computer, [])
    goto(security_checkpoint, moves, computer)
    spoof_identity(computer)

    t.join()


deploy_droid()
