from collections import deque
from typing import List


def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    """
    Time: O(n)
    Space: O(n)
        n - number of rooms
    """
    q = deque([0])
    seen = set()
    n = len(rooms)

    while q:
        room = q.popleft()
        if room in seen:
            continue

        seen.add(room)
        for unlocked in rooms[room]:
            if unlocked not in seen:
                q.append(unlocked)

    return len(seen) == n
