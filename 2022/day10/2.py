def load():
    with open("input") as f:
        for instr in map(lambda x: x.strip().split(" "), f):
            yield (instr[0], 0) if len(instr) == 1 else (instr[0], int(instr[1]))


def get_cycles(instr):
    if instr == "noop":
        return 1
    elif instr == "addx":
        return 2


def execute(program, num_cycles):
    cpu_register, cycle_counter = 1, 1
    instr, param, counter = None, None, 0
    for _ in range(num_cycles):
        yield cycle_counter, cpu_register
        if counter == 0:
            instr, param = next(program)
            counter = get_cycles(instr)
        elif counter == 1:
            if instr == "noop":
                pass
            elif instr == "addx":
                cpu_register += param
        cycle_counter += 1
        counter -= 1


def draw(sprite, cycle, screen):
    if sprite - 1 <= (cycle - 1) % 40 <= sprite + 1:
        screen[cycle-1] = "#"


def render(screen):
    for i, pixel in enumerate(screen):
        print(pixel, end="")
        if (i + 1) % 40 == 0:
            print()


def run_program():
    screen = ["."] * 240
    for cycle, sprite in execute(load(), 240):
        draw(sprite, cycle, screen)
    return screen


render(run_program())
