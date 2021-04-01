import bisect
import heapq


class ExamRoomPQ:
    """
    Max heap
    """

    def __init__(self, N):
        self.N = N
        self.pq = [(self.dist(-1, N), -1, N)]  # max heap

    def seat(self):
        """
        Time: O(log n)
        """
        # current max interval
        _, x, y = heapq.heappop(self.pq)

        if x == -1:
            seat = 0
        elif y == self.N:
            seat = self.N - 1
        else:
            seat = (x + y) // 2

        # push two intervals by breaking at seat
        heapq.heappush(self.pq, (self.dist(x, seat), x, seat))
        heapq.heappush(self.pq, (self.dist(seat, y), seat, y))

        return seat

    def leave(self, p):
        """
        Time: O(n)
        """
        head = tail = None
        for d, x, y in self.pq:
            if x == p:
                tail = (d, x, y)
            if y == p:
                head = (d, x, y)
            if head and tail:
                break

        # O(n)
        self.pq.remove(head)
        self.pq.remove(tail)

        # O(n)
        # Restore heap after the deletion
        heapq.heapify(self.pq)

        # O(log n)
        heapq.heappush(self.pq, (self.dist(head[1], tail[2]), head[1], tail[2]))

    def dist(self, x, y):
        """
        Length of the interval [x, y]
        """
        if x == -1:
            return -y
        elif y == self.N:
            return -(self.N - 1 - x)
        else:
            return -(abs(x - y) // 2)


class ExamRoom:
    """
    Similar to LC849

    There is a solution with O(log n) time complexity,
    for both seat and leave using OrderedDict / TreeSet.
    But it's overly complex for the problem.
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
