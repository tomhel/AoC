def load():
    with open("input") as f:
        graph = {}

        for x in f:
            a, b = x.strip().split("-")
            nodes = graph.get(a, [])
            nodes.append(b)
            graph[a] = nodes
            nodes = graph.get(b, [])
            nodes.append(a)
            graph[b] = nodes

        return graph


def traverse(node, visited, caves):
    if node == "end":
        return 1
    elif node in visited and (node == "start" or 2 in visited.values()):
        return 0
    elif node == node.lower():
        v = visited.get(node, 0) + 1
        visited[node] = v

    return sum(traverse(n, dict(visited), caves) for n in caves[node])


print(traverse("start", {}, load()))
