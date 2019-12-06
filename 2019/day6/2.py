#!/usr/bin/env python3


def find_santa(network, current, depth, parent):
    routes = network.get(current, [])
    
    if "SAN" in routes:
        return depth

    depths = list(filter(None, (find_santa(network, r, depth + 1, current) for r in routes if r != parent)))
    return None if len(depths) == 0 else min(depths)


def find_you(network):
    for node, routes in network.items():
        if "YOU" in routes:
            return node


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
print(find_santa(nw, find_you(nw), 0, None))
