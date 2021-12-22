def load():
    with open("input") as f:
        for x in f:
            flag, cuboid = x.strip().split(" ")
            xx, yy, zz = (d[2:] for d in cuboid.split(","))
            yield flag == "on", [tuple(map(int, d.split(".."))) for d in (xx, yy, zz)]


def intersection(x, y, z):
    cuboid = []
    for a, b in (x, y, z):
        if -50 > b or 50 < a:
            return None
        cuboid.append((max(a, -50), min(b, 50)))
    return cuboid


def reboot():
    cubes = set()

    for on, cuboid in load():
        sub_cuboid = intersection(*cuboid)
        if sub_cuboid is None:
            continue
        xx, yy, zz = sub_cuboid
        for x in range(xx[0], xx[1] + 1):
            for y in range(yy[0], yy[1] + 1):
                for z in range(zz[0], zz[1] + 1):
                    if on:
                        cubes.add((x, y, z))
                    else:
                        cubes.discard((x, y, z))

    return len(cubes)


print(reboot())
