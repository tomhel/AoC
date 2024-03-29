def load():
    with open("input") as f:
        stacks = {}
        for line in f:
            if line.strip() == "":
                break
            for i in range(0, len(line), 4):
                if line[i] == "[":
                    crates = stacks.get(i // 4, [])
                    crates.insert(0, line[i + 1])
                    stacks[i // 4] = crates
        yield stacks
        for line in f:
            _, cnt, _, frm, _, to = line.strip().split(" ")
            yield int(cnt), int(frm) - 1, int(to) - 1


def move(cnt, frm, to, stacks):
    crates = [stacks[frm].pop() for _ in range(cnt)]
    stacks[to].extend(crates)


def rearrange():
    data = load()
    stacks = next(data)
    for cnt, frm, to in data:
        move(cnt, frm, to, stacks)
    return "".join(stacks[i][-1] for i in sorted(stacks))


print(rearrange())
