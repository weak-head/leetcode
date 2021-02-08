from typing import List


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        if value:
            self.is_int = True
            self.value = value
        else:
            self.is_int = False
            self.value = []

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return self.is_int

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        if self.is_int:
            self.is_int = False
            self.value = []
        self.value.append(elem)

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        if not self.is_int:
            self.is_int = True
        self.value = value

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        return self.value

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        return self.value


def depthSumInverse(nestedList: List[NestedInteger]) -> int:
    """
    Flatten the nested lists into unweighted sums.
    Adjust sums based on weight.

    Time: O(n)
    Space: O(m)
        n - total number of elements in the nested lists
        m - max depth of the nested lists
    """
    sums = []

    def extract(ni, d):
        if ni.isInteger():
            while d >= len(sums):
                sums.append(0)
            sums[d] += ni.getInteger()
        else:
            for n in ni.getList():
                extract(n, d + 1)

    for ni in nestedList:
        extract(ni, 0)

    s, n = 0, len(sums)
    for i, v in enumerate(sums):
        s += v * (n - i)

    return s
