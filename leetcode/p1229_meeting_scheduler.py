from typing import List
import heapq


def minAvailableDuration(
    slots1: List[List[int]], slots2: List[List[int]], duration: int
) -> List[int]:
    """
    O(n * log(n))
    """
    slots1.sort()
    slots2.sort()

    i, j = 0, 0
    while i < len(slots1) and j < len(slots2):
        head = max(slots1[i][0], slots2[j][0])
        tail = min(slots1[i][1], slots2[j][1])

        if tail - head >= duration:
            return [head, head + duration]

        if slots1[i][1] < slots2[j][1]:
            i += 1
        else:
            j += 1

    return []


def minAvailableDuration2(
    slots1: List[List[int]], slots2: List[List[int]], duration: int
) -> List[int]:
    """
    O(n * log(n))
    """
    s = list(filter(lambda slot: slot[1] - slot[0] >= duration, slots1 + slots2))
    heapq.heapify(s)
    while len(s) > 1:
        if heapq.heappop(s)[1] >= s[0][0] + duration:
            return [s[0][0], s[0][0] + duration]
    return []
