def load():
    with open("input") as f:
        for instr in map(lambda x: x.strip().split(" "), f):
            yield (instr[0], 0) if len(instr) == 1 else (instr[0], int(instr[1]))


def get_cycles(instr):
    if instr == "noop":
        return 1
    elif instr == "addx":
        return 2


def execute(program):
    cpu_register, cycle_counter = 1, 1
    instr, param, counter = None, None, 0
    while True:
        yield cycle_counter, cpu_register
        if counter == 0:
            instr, param = next(program, ("halt", 0))
            if instr == "halt":
                break
            counter = get_cycles(instr)
        elif counter == 1:
            if instr == "noop":
                pass
            elif instr == "addx":
                cpu_register += param
        cycle_counter += 1
        counter -= 1


def sum_signal_strengths():
    return sum(c * v for c, v in execute(load()) if c in (20, 60, 100, 140, 180, 220))


print(sum_signal_strengths())
