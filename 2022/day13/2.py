from functools import cmp_to_key
import json


def load():
    with open("input") as f:
        packet = []
        for row in f:
            if row.strip() == "":
                yield packet
                packet = []
                continue
            packet.append(json.loads(row))
        yield packet


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


def find_decoder_key():
    div_pkt1, div_pkt2 = [[2]], [[6]]
    packets = [div_pkt1, div_pkt2]
    for pkt1, pkt2 in load():
        packets.append(pkt1)
        packets.append(pkt2)
    packets = sorted(packets, key=cmp_to_key(compare))
    return (packets.index(div_pkt1) + 1) * (packets.index(div_pkt2) + 1)


print(find_decoder_key())
