def load():
    with open("input") as f:
        for row in f:
            yield tuple(int(x) for x in row.strip().split(","))


def get_bounds(cubes):
    minx, miny, minz = min(x for x, _, _ in cubes), min(y for _, y, _ in cubes), min(z for _, _, z in cubes)
    maxx, maxy, maxz = max(x for x, _, _ in cubes), max(y for _, y, _ in cubes), max(z for _, _, z in cubes)
    return minx, miny, minz, maxx, maxy, maxz


def is_air_pocket(x, y, z, cubes, bounds):
    minx, miny, minz, maxx, maxy, maxz = bounds
    q, visited = [(x, y, z)], set()
    while len(q) > 0:
        x, y, z = q.pop(0)
        if (x, y, z) in visited or (x, y, z) in cubes:
            continue
        visited.add((x, y, z))
        if x <= minx or x >= maxx or y <= miny or y >= maxy or z <= minz or z >= maxz:
            return False
        for dx, dy, dz in ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)):
            q.append((x + dx, y + dy, z + dz))
    return True


def exterior_surface_area():
    cubes = set(load())
    bounds = get_bounds(cubes)
    count = 0
    for x, y, z in cubes:
        for dx, dy, dz in ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)):
            a, b, c = x + dx, y + dy, z + dz
            if (a, b, c) not in cubes and not is_air_pocket(a, b, c, cubes, bounds):
                count += 1
    return count


# takes about 5 seconds to run.
print(exterior_surface_area())
