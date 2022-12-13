def load():
    with open("input") as f:
        packet = []
        for row in f:
            if row.strip() == "":
                yield packet
                packet = []
                continue
            packet.append(row.strip())
        yield packet


def parse_list(packet):
    balanced = ["["]
    res = ""
    for token in packet:
        if token == "[":
            balanced.append("[")
        elif token == "]":
            balanced.pop()
        if len(balanced) == 0:
            break
        res += token
    return res


def parse_packet(packet):
    res, skip_to = [], 0
    for i, token in enumerate(packet):
        if i < skip_to or token == ",":
            continue
        elif token.isdigit():
            for k in range(i + 1, len(packet)):
                if packet[k].isdigit():
                    token += packet[k]
                else:
                    break
            res.append(int(token))
            skip_to = i + len(token)
        elif token == "[":
            sub_packet = parse_list(packet[i+1:])
            sub_res = parse_packet(sub_packet)
            skip_to = i + len(sub_packet) + 1
            res.append(sub_res)
    return res


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, list) and isinstance(right, list):
        i = 0
        while True:
            if i >= len(left) or i >= len(right):
                return len(left) - len(right)
            res = compare(left[i], right[i])
            if res != 0:
                return res
            i += 1


def get_packet(packet):
    return parse_packet(packet)[0]


def sum_indices_of_correct_order():
    return sum(i + 1 for i, pkt in enumerate(load()) if compare(get_packet(pkt[0]), get_packet(pkt[1])) <= 0)


print(sum_indices_of_correct_order())
