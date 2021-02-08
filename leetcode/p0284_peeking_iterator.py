class Iterator:
    def __init__(self, nums):
        self.collection = nums
        self.index = 0

    def hasNext(self):
        return self.index < len(self.collection)

    def next(self):
        v = self.collection[self.index]
        self.index += 1
        return v


class PeekingIterator:
    def __init__(self, iterator):
        self._it = iterator
        self._val = None
        self.next()

    def peek(self):
        return self._val

    def next(self):
        r = self._val
        self._val = self._it.next() if self._it.hasNext() else None
        return r

    def hasNext(self):
        return self._val is not None
