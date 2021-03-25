from typing import List
from collections import deque


def pacificAtlantic(matrix: List[List[int]]) -> List[List[int]]:
    """
    BFS

    Time: O(m * n)
    Space: O(m * n)
    """
    if not matrix or not matrix[0]:
        return []

    def bfs(q):
        seen = set()
        while q:
            r, c = q.popleft()

            if (r, c) in seen:
                continue

            seen.add((r, c))

            for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) in seen:
                    continue
                if (
                    0 <= nr < len(matrix)
                    and 0 <= nc < len(matrix[0])
                    and matrix[nr][nc] >= matrix[r][c]
                ):
                    q.append((nr, nc))
        return seen

    q1 = deque()
    q2 = deque()

    for i in range(len(matrix)):
        q1.append((i, 0))
        q2.append((i, len(matrix[0]) - 1))

    for i in range(len(matrix[0])):
        q1.append((0, i))
        q2.append((len(matrix) - 1, i))

    r1 = bfs(q1)
    r2 = bfs(q2)

    return r1.intersection(r2)
