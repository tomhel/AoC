def load():
    with open("input") as f:
        for x in f:
            a, b, = x.strip().split("|")
            yield {frozenset(x) for x in a.strip().split()}, [frozenset(x) for x in b.strip().split()]


def decode_signal(signal):
    num = {}

    while len(num) < 10:
        for x in signal.difference(num.values()):
            if len(x) == 2:
                num[1] = x
            elif len(x) == 3:
                num[7] = x
            elif len(x) == 4:
                num[4] = x
            elif len(x) == 7:
                num[8] = x
            elif len(x) == 6 and 4 in num and num[4].issubset(x):
                num[9] = x
            elif len(x) == 5 and 1 in num and num[1].issubset(x):
                num[3] = x
            elif len(x) == 6 and 7 in num and 9 in num and num[7].issubset(x) and num[9] != x:
                num[0] = x
            elif len(x) == 6 and 1 in num and not num[1].issubset(x):
                num[6] = x
            elif len(x) == 5 and 6 in num and x.issubset(num[6]):
                num[5] = x
            elif len(x) == 5 and 3 in num and 5 in num:
                num[2] = x

    return {v: k for k, v in num.items()}


def decode_output():
    result = 0

    for sig, out in load():
        mapping = decode_signal(sig)
        result += int("".join(str(mapping[x]) for x in out))

    return result


print(decode_output())
