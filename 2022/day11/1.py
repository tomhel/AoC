from dataclasses import dataclass


@dataclass
class Monkey:
    n: int
    items: list = None
    operation: tuple = None
    test: int = None
    throw_true: int = None
    throw_false: int = None
    inspections: int = 0


def load():
    with open("input") as f:
        monkey = None
        for line in (x.strip() for x in f):
            if line.startswith("Monkey"):
                if monkey:
                    yield monkey
                monkey = Monkey(n=int(line.split()[1][-2]))
            if line.startswith("Starting items:"):
                monkey.items = list(int(x.strip()) for x in line.split(":")[1].split(","))
            elif line.startswith("Operation:"):
                monkey.operation = tuple(int(x) if x.isdigit() else x for x in line.split("=")[1].strip().split())
            elif line.startswith("Test:"):
                monkey.test = int(line.split()[-1])
            elif line.startswith("If true:"):
                monkey.throw_true = int(line.split()[-1])
            elif line.startswith("If false:"):
                monkey.throw_false = int(line.split()[-1])
        yield monkey


def get_worry_level(item, operation):
    a, op, b = operation
    a = item if a == "old" else a
    b = item if b == "old" else b
    return a * b if op == "*" else a + b


def test_throw(item, divisor):
    return item % divisor == 0


def calc_monkey_business():
    monkeys = {m.n: m for m in load()}
    for _ in range(20):
        for i in sorted(monkeys):
            m = monkeys[i]
            for _ in range(len(m.items)):
                if len(m.items) > 0:
                    item = m.items.pop(0)
                    m.inspections += 1
                    worry_level = get_worry_level(item, m.operation) // 3
                    if test_throw(worry_level, m.test):
                        monkeys[m.throw_true].items.append(worry_level)
                    else:
                        monkeys[m.throw_false].items.append(worry_level)
    m1, m2 = sorted(monkeys.values(), key=lambda k: k.inspections)[-2:]
    return m1.inspections * m2.inspections


print(calc_monkey_business())
