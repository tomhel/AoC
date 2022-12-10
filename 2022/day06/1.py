def load():
    with open("input") as f:
        return f.read().strip()


def find_packet_marker():
    data = load()
    for i in range(len(data) - 3):
        if len(set(data[i:i+4])) == 4:
            return i + 4


print(find_packet_marker())
