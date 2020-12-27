from typing import List
import heapq


def minMeetingRooms(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    events = []
    for event in intervals:
        events.append((event[0], 1))  # beginning +1, preseeds during sort
        events.append((event[1], -1))  # end -1
    events.sort()

    max_rooms, used_rooms = 0, 0
    for event in events:
        used_rooms += event[1]
        max_rooms = max(max_rooms, used_rooms)

    return max_rooms


def minMeetingRooms2(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])

    free_rooms = []
    heapq.heappush(free_rooms, intervals[0][1])

    for i in intervals[1:]:
        if free_rooms[0] <= i[0]:
            heapq.heappop(free_rooms)

        heapq.heappush(free_rooms, i[1])

    return len(free_rooms)


def minMeetingRooms3(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    used_rooms = 0

    start_timings = sorted([i[0] for i in intervals])
    end_timings = sorted(i[1] for i in intervals)
    L = len(intervals)

    end_pointer = 0
    start_pointer = 0

    while start_pointer < L:
        if start_timings[start_pointer] >= end_timings[end_pointer]:
            used_rooms -= 1
            end_pointer += 1

        used_rooms += 1
        start_pointer += 1

    return used_rooms
