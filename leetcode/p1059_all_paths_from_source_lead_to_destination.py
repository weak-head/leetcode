from collections import defaultdict
from typing import List


def leadsToDestination(edges: List[List[int]], source: int, destination: int) -> bool:
    """
    Time: O(v + e)
    Space: O(v + e)
        v - number of vertices
        e - number of edges
    """
    seen = {}
    graph = defaultdict(list)

    for f, t in edges:
        graph[f].append(t)

    def dfs(node):

        if node in seen:
            return seen[node] == "done"

        if not graph[node]:
            return node == destination

        seen[node] = "active"
        for connection in graph[node]:
            if not dfs(connection):
                return False

        seen[node] = "done"
        return True

    return dfs(source)
