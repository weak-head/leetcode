from typing import List


def canAttendMeetings(intervals: List[List[int]]) -> bool:
    """
    O(n * log(n))
    """
    intervals.sort()
    for i in range(1, len(intervals)):
        if intervals[i - 1][1] > intervals[i][0]:
            return False
    return True
