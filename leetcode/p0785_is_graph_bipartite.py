from typing import List


def isBipartite(graph: List[List[int]]) -> bool:
    """
    DFS with coloring

    Time: (e + v)
    Space: (v)
        e - number of edges
        v - number of vertices
    """
    split = {}

    def dfs(i, g):
        if i in split:
            return split[i] == g

        split[i] = g
        for neighbor in graph[i]:
            if not dfs(neighbor, not g):
                return False

        return True

    for i in range(len(graph)):
        if i not in split:
            if not dfs(i, False):
                return False

    return True
