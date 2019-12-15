#!/usr/bin/env python3


def find_santa(network, current, depth, parent):
    routes = network.get(current, [])
    
    if "SAN" in routes:
        return depth

    depths = [find_santa(network, r, depth + 1, current) for r in routes if r != parent]
    return float("inf") if len(depths) == 0 else min(depths)


def construct_network(orbits):
    network = {}

    for src, dst in orbits:
        routes = network.get(src, [])
        routes.append(dst)
        network[src] = routes
        routes = network.get(dst, [])
        routes.append(src)
        network[dst] = routes

    return network


data = (x.strip().split(")") for x in open("input"))
nw = construct_network(data)
print(find_santa(nw, nw["YOU"][0], 0, None))
