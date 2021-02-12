import random


class RandomizedSet:
    def __init__(self):
        self.d = {}
        self.a = []

    def insert(self, val: int) -> bool:
        """
        Time: O(1)
        Space: O(1)
        """
        if val in self.d:
            return False

        self.a.append(val)
        self.d[val] = len(self.a) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Time: O(1)
        Space: O(1)
        """
        if val not in self.d:
            return False

        ix = self.d[val]
        self.d[self.a[-1]] = ix

        self.a[ix], self.a[-1] = self.a[-1], self.a[ix]

        del self.d[val]
        del self.a[-1]
        return True

    def getRandom(self) -> int:
        """
        Time: O(1)
        Space: O(1)
        """
        return self.a[random.randint(0, len(self.a) - 1)]
