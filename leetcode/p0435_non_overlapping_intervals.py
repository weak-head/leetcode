from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    """
    Greedy
    We always want to base our pick based
    on the earliest end time.

    Time: O(n)
    Space: O(1)
        n - number of intervals
    """
    if not intervals:
        return 0

    intervals = sorted(intervals, key=lambda x: x[1])

    count = 0
    current_end = intervals[0][1]
    for start, end in intervals[1:]:
        if start < current_end:
            count += 1
        else:
            current_end = end

    return count
