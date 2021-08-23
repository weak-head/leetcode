from collections import defaultdict


def allPathsSourceTarget(g):
    """
    DFS

    Time: O( (2^v) * (v+e) )
    Space: O( (2^v) * v )
        v - number of vertices
        e - number of edges
    """

    target = len(g) - 1
    graph = defaultdict(set)
    seen = set()
    res = []

    for v1 in range(len(g)):
        for v2 in g[v1]:
            graph[v1].add(v2)

    def dfs(node, path):
        if node is None:
            return

        if node == target:
            res.append(tuple(path))

        for child in graph[node]:
            if child not in seen:
                seen.add(child)
                dfs(child, path + [child])
                seen.remove(child)

    seen.add(0)
    dfs(0, [0])

    return res


def allPathsSourceTarget_bfs(graph):
    if not graph:
        return

    size = len(graph)
    paths = []

    stack = [(0, [0])]

    while stack:
        start, path = stack.pop()

        if start == size - 1:
            paths.append(path)

        for nei in graph[start]:
            stack.append((nei, path + [nei]))

    return map(tuple, paths)
