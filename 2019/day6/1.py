#!/usr/bin/env python3


def calc_orbits(network, current, depth):
    routes = network.get(current, [])
    return sum(calc_orbits(network, r, depth + 1) for r in routes) + depth
    

def construct_network(orbits):
    network = {}

    for src, dst in orbits:
        routes = network.get(src, [])
        routes.append(dst)
        network[src] = routes

    return network


data = (x.strip().split(")") for x in open("input"))
nw = construct_network(data)
print(calc_orbits(nw, "COM", 0))
