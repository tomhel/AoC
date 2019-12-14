#!/usr/bin/env python3


import re


def calc_ore_count(reaction_graph, product, amount, stash):
    count, dependencies = reaction_graph.get(product)
    reserve = stash.get(product, 0)

    while amount > 0 and reserve > 0:
        reserve -= 1
        amount -= 1

    stash[product] = reserve
    ore_count = 0

    while amount > 0:
        amount -= count

        for n, chem in dependencies:
            if chem == "ORE":
                ore_count += n
                continue

            ore_count += calc_ore_count(reaction_graph, chem, n, stash)

    stash[product] += abs(amount)
    return ore_count


def construct_graph(reactions):
    reaction_graph = {}

    for r in reactions:
        in_chems, out_amount, out_chem = r[:-1], r[-1][0], r[-1][1]
        reaction_graph[out_chem] = (out_amount, in_chems)

    return reaction_graph


def load_input():
    for row in [re.findall("\d+ [A-Z]+", x) for x in open("input")]:
        yield [(int(a), b) for a, b in (r.split(" ") for r in row)]


graph = construct_graph(load_input())
print(calc_ore_count(graph, "FUEL", 1, {}))
