from collections import deque
from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Topological sorting

    Time: O(v + e)
    Space: O(v + e)
    """

    # -- Graph and in-degree
    graph = {i: [] for i in range(numCourses)}
    in_degree = {i: 0 for i in range(numCourses)}

    for f, t in prerequisites:
        graph[f].append(t)
        in_degree[t] += 1

    # -- Nodes with 0 in-degree
    q = deque([node for node, degree in in_degree.items() if degree == 0])

    while q:
        node = q.popleft()

        for dependency in graph[node]:
            in_degree[dependency] -= 1
            if in_degree[dependency] == 0:
                q.append(dependency)

    # -- Cycle detection
    for degree in in_degree.values():
        if degree != 0:
            return False

    return True
