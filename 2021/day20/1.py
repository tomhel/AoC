def load():
    with open("input") as f:
        yield next(f).strip()
        next(f)
        img = {}
        for y, row in enumerate(f):
            img.update({(x, y): v for x, v in enumerate(row.strip())})
        yield img


def get_square(x, y, image, void_value):
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            yield image.get((j, i), void_value)


def to_decimal(square):
    return int("".join("1" if p == "#" else "0" for p in square), 2)


def apply_enhancement(image, algorithm, void_value):
    new_image = {}
    p1, p2 = min(image), max(image)

    for y in range(p1[1] - 2, p2[1] + 3):
        for x in range(p1[0] - 2, p2[0] + 3):
            index = to_decimal(get_square(x, y, image, void_value))
            new_image[(x, y)] = algorithm[index]

    return new_image


def get_void_value(algorithm, iteration):
    return "." if iteration % 2 == 0 or algorithm[0] == "." else "#"


def run_algorithm(iterations):
    algorithm, image = load()

    for i in range(iterations):
        image = apply_enhancement(image, algorithm, get_void_value(algorithm, i))

    return sum(1 for p in image.values() if p == "#")


print(run_algorithm(2))
