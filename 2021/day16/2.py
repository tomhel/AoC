from functools import reduce
from operator import mul


def load():
    mapping = {
        "0": "0000", "1": "0001", "2": "0010", "3": "0011",
        "4": "0100", "5": "0101", "6": "0110", "7": "0111",
        "8": "1000", "9": "1001", "A": "1010", "B": "1011",
        "C": "1100", "D": "1101", "E": "1110", "F": "1111"
    }
    with open("input") as f:
        for x in next(f).strip():
            for bit in mapping[x]:
                yield bit


def read(data, length):
    buffer = "".join(next(data) for _ in range(length))
    if len(buffer) != length:
        raise StopIteration
    return buffer


def decode_packets(data):
    try:
        version = int(read(data, 3), 2)
        typeid = int(read(data, 3), 2)
    except StopIteration:
        return None

    if typeid == 4:  # literal
        value = ""
        while True:
            prefix = read(data, 1)
            value += read(data, 4)
            if prefix == "0":
                break
        return version, typeid, int(value, 2)
    else:  # operator
        lentypeid = read(data, 1)
        if lentypeid == "0":  # read sub packets based on length
            subpktlen = int(read(data, 15), 2)
            subdata = iter(read(data, subpktlen))
            packets = []
            while True:
                pkt = decode_packets(subdata)
                if pkt is None:
                    break
                packets.append(pkt)
            return version, typeid, packets
        elif lentypeid == "1":  # read sub packets based on count
            subpktcnt = int(read(data, 11), 2)
            return version, typeid, [decode_packets(data) for _ in range(subpktcnt)]


def evaluate_expr(packets):
    _, typeid, body = packets

    if typeid == 4:  # literal
        return body
    elif typeid == 0:  # sum
        return sum(evaluate_expr(pkt) for pkt in body)
    elif typeid == 1:  # product
        return reduce(mul, (evaluate_expr(pkt) for pkt in body))
    elif typeid == 2:  # minimum
        return min(evaluate_expr(pkt) for pkt in body)
    elif typeid == 3:  # maximum
        return max(evaluate_expr(pkt) for pkt in body)
    elif typeid == 5:  # greater than
        return int(evaluate_expr(body[0]) > evaluate_expr(body[1]))
    elif typeid == 6:  # less than
        return int(evaluate_expr(body[0]) < evaluate_expr(body[1]))
    elif typeid == 7:  # equal to
        return int(evaluate_expr(body[0]) == evaluate_expr(body[1]))
    else:
        raise Exception(f"unknown typeid {typeid}")


def decode_transmission():
    transmission = load()
    return evaluate_expr(decode_packets(transmission))


print(decode_transmission())
