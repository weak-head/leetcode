from typing import List
from collections import deque


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    Topological sorting

    Time: O(v + e)
    Space: O(v + e)
    """
    graph = {i: [] for i in range(numCourses)}
    in_degree = {i: 0 for i in range(numCourses)}
    for f, t in prerequisites:
        graph[f].append(t)
        in_degree[t] += 1

    q = deque([node for node, degree in in_degree.items() if degree == 0])
    r = deque()

    while q:
        node = q.popleft()
        r.appendleft(node)

        for dependency in graph[node]:
            in_degree[dependency] -= 1
            if in_degree[dependency] == 0:
                q.append(dependency)

    for degree in in_degree.values():
        if degree != 0:
            return []

    return r
