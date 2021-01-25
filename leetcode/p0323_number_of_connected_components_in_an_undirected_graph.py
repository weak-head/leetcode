from typing import List
from collections import deque


def countComponents_dfs(n: int, edges: List[List[int]]) -> int:
    """
    DFS or BFS from any node completely covers
    one strongly connected component in undirected graph.

    Time: O(v + e)
    Space: O(v + e)
    """

    def dfs(node):
        if visited[node]:
            return
        visited[node] = True

        for child in adj_list[node]:
            dfs(child)

    # build adjacency list
    adj_list = {i: [] for i in range(n)}
    for v1, v2 in edges:
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    visited = [False] * n
    components = 0
    for node in range(n):
        if not visited[node]:
            dfs(node)
            components += 1

    return components


def countComponents_bfs(n: int, edges: List[List[int]]) -> int:
    """
    DFS or BFS from any node completely covers
    one strongly connected component in undirected graph.

    Time: O(v + e)
    Space: O(v + e)
    """

    def bfs(node):
        q = deque([node])

        while q:
            n = q.popleft()
            if visited[n]:
                continue

            visited[n] = True
            for child in adj_list[n]:
                q.append(child)

    # build adjacency list
    adj_list = {i: [] for i in range(n)}
    for v1, v2 in edges:
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    visited = [False] * n
    components = 0
    for node in range(n):
        if not visited[node]:
            bfs(node)
            components += 1

    return components


def countComponents_sets(n: int, edges: List[List[int]]) -> int:
    """
    Disjoint-set / Union-find
    https://en.wikipedia.org/wiki/Disjoint-set_data_structure

    Union by rank + path compression

    Time: O(v + e)
    """

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(xy):
        x, y = map(find, xy)
        if rank[x] < rank[y]:
            parent[x] = y
        else:
            parent[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

    parent, rank = list(range(n)), [0] * n
    list(map(union, edges))  # force iterator to evaluate

    return len({find(x) for x in parent})
