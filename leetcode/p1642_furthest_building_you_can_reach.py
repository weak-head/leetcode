import heapq
from typing import List


def furthestBuilding(heights: List[int], bricks: int, ladders: int) -> int:
    """
    Greedy,
    We should use ladders for the biggest altitude changes.
    We should fallback to bricks when there are no more ladders.
    We can replace used ladders with bricks, when we find better candidates.

    Time: O(n * log(n))
    Space: O(n)
        n - length of the array
    """
    used_ladders, used_bricks = [], 0

    for building in range(len(heights) - 1):
        # no need to use ladders or bricks
        if heights[building + 1] < heights[building]:
            continue

        heapq.heappush(used_ladders, heights[building + 1] - heights[building])

        if len(used_ladders) > ladders:
            bricks_required = heapq.heappop(used_ladders)
            if bricks_required + used_bricks > bricks:
                return building
            else:
                used_bricks += bricks_required

    return len(heights) - 1
