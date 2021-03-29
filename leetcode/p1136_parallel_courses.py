from collections import deque
from typing import List


def minimumSemesters(n: int, relations: List[List[int]]) -> int:
    """
    Topological sorting,
    Kahn's algorithm

    Similar to:
        - LC269 - alien dictionary

    Time: O(v + e)
    Space: O(v + e)
        v - vertices
        e - edges
    """

    # -- Compose graph with in-degree
    graph = {i: [] for i in range(1, n + 1)}
    in_degree = {i: 0 for i in range(1, n + 1)}

    for f, t in relations:
        graph[f].append(t)
        in_degree[t] += 1

    # -- Start with all nodes having 0 in-degree
    q = deque([node for node, degree in in_degree.items() if degree == 0])

    # -- Topological sorting
    semester = 0
    while q:
        semester += 1
        next_q = deque()
        while q:
            node = q.popleft()
            for connection in graph[node]:
                in_degree[connection] -= 1
                if in_degree[connection] == 0:
                    next_q.append(connection)
        q = next_q

    # -- Cycle check
    for degree in in_degree.values():
        if degree != 0:
            return -1

    return semester
