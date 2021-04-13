from typing import List


class NestedInteger:
    def __init__(self, value) -> None:
        if type(value) == int:
            self.value = value
        else:
            self.value = [NestedInteger(nl) for nl in value]

    def isInteger(self) -> bool:
        return type(self.value) == int

    def getInteger(self) -> int:
        return self.value

    def getList(self) -> List["NestedInteger"]:
        return self.value


class NestedIterator:
    def __init__(self, nestedList):
        """
        Lazy iterator over the nested list.
        """
        self.stack = [[nestedList, 0]]

    def next(self):
        """
        Worst case time: O(n)
        Amortized time: O(1)
        Space: O(n)
        """
        self.hasNext()
        nl, ix = self.stack[-1]
        self.stack[-1][1] += 1
        return nl[ix].getInteger()

    def hasNext(self):
        """
        Worst cast time: O(n)
        Amortized time: O(1)
        Space: O(n)
            n - number of elements in the nested list
        """
        while self.stack:
            nl, ix = self.stack[-1]

            if ix == len(nl):
                self.stack.pop()
            else:
                if nl[ix].isInteger():
                    return True
                self.stack[-1][1] += 1
                self.stack.append([nl[ix].getList(), 0])
        return False
