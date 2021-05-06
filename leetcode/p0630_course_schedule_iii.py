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
    courses = sorted(courses, key=lambda x: x[1])
    best_courses = []
    total_duration = 0

    for duration, last_day in courses:

        # take this course and save it's duration into the priority queue
        if total_duration + duration <= last_day:
            total_duration += duration
            heapq.heappush(best_courses, -duration)

        # replace the previous longest course with this one
        # if this one is shorter
        elif len(best_courses) and -best_courses[0] > duration:
            previous_longest = heapq.heappop(best_courses)  # negated
            total_duration += previous_longest + duration
            heapq.heappush(best_courses, -duration)

    return len(best_courses)
