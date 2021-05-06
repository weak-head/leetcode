import heapq
from typing import List


def scheduleCourse(courses: "List[List[int]]") -> "int":
    """
    Greedy, priority queue

    Similar thinking to:
        - LC300 - LIS

    Time: O(n * log n)
    Space: O(n)
    """
    # (last_day, duration)
    courses = sorted(map(lambda x: [x[1], x[0]], courses))

    pq = []
    can_take = 0
    total_duration = 0

    for last_day, duration in courses:

        # take this course and save it's duration into the priority queue
        if total_duration + duration <= last_day:
            can_take += 1
            total_duration += duration
            heapq.heappush(pq, -duration)

        # replace the previous longest course with this one
        # if this one is shorter
        elif len(pq) and -pq[0] > duration:
            previous_longest = heapq.heappop(pq)  # negated
            total_duration += previous_longest + duration
            heapq.heappush(pq, -duration)

    return can_take
