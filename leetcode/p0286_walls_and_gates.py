from typing import List
from collections import deque


def wallsAndGates(rooms: List[List[int]]) -> None:
    """
    BFS from all gates at the same time

    Time: O(r * c)
    """
    EMPTY, GATE = 2147483647, 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    q = deque()
    for r in range(len(rooms)):
        for c in range(len(rooms[r])):
            if rooms[r][c] == GATE:
                q.append((r, c))

    while q:
        r, c = q.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (
                (nr < 0)
                or (nc < 0)
                or (nr >= len(rooms))
                or (nc >= len(rooms[nr]))
                or (rooms[nr][nc] != EMPTY)
            ):
                continue

            rooms[nr][nc] = rooms[r][c] + 1
            q.append((nr, nc))
