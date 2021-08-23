from typing import List
from collections import defaultdict, deque


def validTree(n: int, edges: List[List[int]]) -> bool:
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
