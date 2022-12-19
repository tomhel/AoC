from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Robot:
    type: str
    materials: List[Tuple[int, str]]


@dataclass
class Blueprint:
    n: int
    robots: List[Robot]


def load():
    with open("input") as f:
        for row in f:
            n, bp = row.strip().split(": ")
            robots = []
            for x in bp[:-1].split(". "):
                a, b = x.split(" robot costs ")
                robot = a.split(" ")[1]
                materials = []
                for c in b.split(" and "):
                    count, material = c.split(" ")
                    materials.append((int(count), material))
                robots.append(Robot(robot, materials))
            yield Blueprint(int(n.split(" ")[1]), robots)


def estimate_max_geodes(t, robots, inventory):
    count = inventory["geode"]
    for tt in range(24 - t):
        count += robots.count("geode")
        robots.append("geode")
    return count


def get_maximum_geode_count(blueprint, inventory, robots, t, states, best):
    if t >= 24:
        best[0] = max(inventory["geode"], best[0])
        return inventory["geode"]
    if estimate_max_geodes(t, list(robots), inventory) <= best[0]:
        return 0
    s = (t, robots.count("ore"), robots.count("clay"), robots.count("obsidian"), robots.count("geode"),
         inventory["ore"], inventory["clay"], inventory["obsidian"], inventory["geode"])
    if s in states:
        return 0
    states.add(s)
    possible_builds = []
    for r in blueprint.robots:
        build = True
        for n, m in r.materials:
            if inventory[m] < n:
                build = False
                break
        if build:
            possible_builds.append(r)
    for m in inventory:
        inventory[m] = inventory[m] + robots.count(m)
    geodes = [0]
    for r in sorted(possible_builds, key=lambda k: {"geode": 0, "obsidian": 1, "clay": 2, "ore": 3}[k.type]):
        inv = dict(inventory)
        for n, m in r.materials:
            inv[m] = inv[m] - n
        geodes.append(get_maximum_geode_count(blueprint, inv, robots + [r.type], t + 1, states, best))
    if len(possible_builds) < len(blueprint.robots):
        geodes.append(get_maximum_geode_count(blueprint, dict(inventory), list(robots), t + 1, states, best))
    return max(geodes)


def blueprint_quality_levels():
    quality = 0
    for blueprint in load():
        inventory = {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0}
        robots = ["ore"]
        q = get_maximum_geode_count(blueprint, inventory, robots, 0, set(), [0])
        quality += q * blueprint.n
    return quality


# takes about 2 minutes to run using PyPy. 7 minutes using CPython.
print(blueprint_quality_levels())
