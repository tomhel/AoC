def load():
    with open("input") as f:
        return f.read().strip()


def find_message_marker():
    data = load()
    for i in range(len(data) - 13):
        if len(set(data[i:i+14])) == 14:
            return i + 14


print(find_message_marker())
