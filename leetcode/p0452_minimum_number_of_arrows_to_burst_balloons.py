from typing import List


def findMinArrowShots(points: List[List[int]]) -> int:
    """
    Greedy
    We want to pick the balloon with the closest end,
    and drop the balloons that overlap it.

    Similar to overlapping/non-overlapping intervals.

    Time: O(n)
    Space: O(1)
        n - number of balloons
    """
    if not points:
        return 0

    points = sorted(points, key=lambda x: x[1])

    arrows = 1
    current_end = points[0][1]
    for start, end in points[1:]:
        if start <= current_end:
            continue
        else:
            arrows += 1
            current_end = end

    return arrows
