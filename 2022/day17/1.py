def load():
    yield [
        # '####'
        ((0, 0), (1, 0), (2, 0), (3, 0)),
        # '.#.'
        # '###'
        # '.#.',
        ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),
        # '..#'
        # '..#'
        # '###'
        ((2, 0), (2, 1), (0, 2), (1, 2), (2, 2)),
        # '#'
        # '#'
        # '#'
        # '#'
        ((0, 0), (0, 1), (0, 2), (0, 3)),
        # '##'
        # '##'
        ((0, 0), (1, 0), (0, 1), (1, 1))
    ]
    with open("input") as f:
        yield list(f.read().strip())


def next_shape(shapes, i):
    return shapes[i % len(shapes)]


def get_dimensions(shape):
    return max(x for x, _ in shape) + 1, max(y for _, y in shape) + 1


def next_yet(pattern, i):
    return -1 if pattern[i % len(pattern)] == "<" else 1


def is_collision(x, y, shape, chamber):
    for a, b in shape:
        if y + b == 0 or (x + a, y + b) in chamber:
            return True
    return False


def add_shape(x, y, shape, chamber):
    for a, b in shape:
        chamber[(x + a, y + b)] = "#"


def simulate_tower():
    shapes, jet_pattern = load()
    left_wall, right_wall, peak = 0, 8, 0
    chamber = {}
    shp_idx, jet_idx = 0, 0
    for _ in range(2022):
        shp = next_shape(shapes, shp_idx)
        shp_idx += 1
        shp_width, shp_height = get_dimensions(shp)
        x, y = left_wall + 3, peak - 3 - shp_height
        while True:
            dx, dy = next_yet(jet_pattern, jet_idx), 1
            jet_idx += 1
            if left_wall < x + dx and right_wall >= x + dx + shp_width and not is_collision(x + dx, y, shp, chamber):
                x += dx
            if is_collision(x, y + dy, shp, chamber):
                add_shape(x, y, shp, chamber)
                peak = min(y, peak)
                break
            y += dy
    return abs(peak)


print(simulate_tower())
