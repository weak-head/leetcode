class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


def employeeFreeTime1(schedule: "[[Interval]]") -> "[Interval]":
    """
    O(n * log(n))
    n - number of all intervals across all employees
    """
    events = []
    for ix, employee in enumerate(schedule):
        for event in employee:
            # (time, ordering, uniqueID)
            events.append((event.start, 1, ix))
            events.append((event.end, 0, ix))

    events.sort()  # by time, then ordering

    breaks = []
    break_start = None
    active = {}
    for time, event_type, employee in events:
        # start
        if event_type == 1:
            if break_start:
                if break_start < time:  # non-empty interval
                    breaks.append((break_start, time))
                break_start = None

            active[employee] = time
        # end
        else:
            del active[employee]

            if not active:
                break_start = time

    return breaks


def employeeFreeTime2(schedule: "[[Interval]]") -> "[Interval]":
    """
    O(n * log(n))
    """
    intervals = sorted([i for s in schedule for i in s], key=lambda x: x.start)
    res, end = [], intervals[0].end
    for i in intervals[1:]:
        if i.start > end:
            res.append((end, i.start))
        end = max(end, i.end)
    return res
