import bisect


class ExamRoom:
    """
    Similar to LC849

    There is a solution with O(log n) time complexity,
    for both seat and leave using OrderedDict / TreeSet.
    """

    def __init__(self, N):
        self.N = N
        self.L = []

    def seat(self):
        """
        Time: O(n)
        """
        N = self.N
        L = self.L
        position = 0

        if L:
            max_distance = L[0]
            # i-1 => start interval
            # i   => end interval
            for start, end in zip(L, L[1:]):
                possible_distance = (end - start) // 2
                if possible_distance > max_distance:
                    max_distance = possible_distance
                    position = start + max_distance

            # check the last position in the array
            if N - 1 - L[-1] > max_distance:
                position = N - 1

        bisect.insort(L, position)
        return position

    def leave(self, p):
        """
        Time: O(n)
        """
        self.L.remove(p)
