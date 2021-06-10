from bisect import bisect_left, insort


class Calendar:
    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        """
        Time: O(n)
        Space: O(1)
        """
        ix = bisect_left(self.events, (start, end))

        # not last
        if ix < len(self.events):
            next_start = self.events[ix][0]
            if next_start < end and next_start >= start:
                return False

        # not first
        if ix != 0:
            prev_end = self.events[ix - 1][1]
            if prev_end > start:
                return False

        insort(self.events, (start, end))
        return True
