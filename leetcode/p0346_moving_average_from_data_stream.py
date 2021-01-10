class MovingAverage:
    def __init__(self, size: int):
        """
        Space: O(size)
        """
        self._size = size
        self._window = [None] * self._size
        self._len = 0
        self._ix = 0
        self._sum = 0

    def next(self, val: int) -> float:
        """
        O(1)
        """
        if self._window[self._ix]:
            self._sum -= self._window[self._ix]

        self._window[self._ix] = val
        self._ix = (self._ix + 1) % self._size
        self._sum += val
        self._len = min(self._size, self._len + 1)

        return self._sum / self._len
