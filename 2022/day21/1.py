def load():
    with open("input") as f:
        for row in f:
            name, expr = row.strip().split(": ")
            yield name, int(expr) if expr.isdigit() else tuple(expr.split(" "))


def yell(m, monkeys):
    expr = monkeys[m]
    if isinstance(expr, int):
        return expr
    m1, op, m2 = expr
    if op == "+":
        return yell(m1, monkeys) + yell(m2, monkeys)
    elif op == "-":
        return yell(m1, monkeys) - yell(m2, monkeys)
    elif op == "*":
        return yell(m1, monkeys) * yell(m2, monkeys)
    elif op == "/":
        return yell(m1, monkeys) / yell(m2, monkeys)


def monkey_number():
    monkeys = {name: expr for name, expr in load()}
    return yell("root", monkeys)


print(monkey_number())
