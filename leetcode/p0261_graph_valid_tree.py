from typing import List
from collections import defaultdict, deque


def validTree_uf(n, edges):
    """
    Union find / Disjoint set

    Time: O(v)
    Space: O(v)
    """

    # Graph should have (n-1) edges to be a valid tree
    if len(edges) != n - 1:
        return False

    parent = list(range(n))
    rank = [1] * n

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(xy):
        x, y = map(find, xy)

        # cycle
        if x == y:
            return False

        if rank[x] < rank[y]:
            parent[x] = y
        else:
            parent[y] = x
            if rank[x] != rank[y]:
                rank[x] += 1

        return True

    for edge in edges:
        if not union(edge):
            return False

    return True


def validTree_bfs(n: int, edges: List[List[int]]) -> bool:
    """
    BFS

    Time: O(v)
    Space: O(v)
    """

    g = defaultdict(set)
    for v1, v2 in edges:
        g[v1].add(v2)
        g[v2].add(v1)

    seen = set()

    def bfs(i):
        q = deque([(i, None)])
        seen.add(i)

        while q:
            node, parent = q.popleft()

            for child in g[node]:
                if child != parent:
                    if child in seen:
                        return False
                    seen.add(child)
                    q.append((child, node))

        return True

    if not bfs(0):
        return False

    return len(seen) == n
