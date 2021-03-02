class MyStack:
    def __init__(self):
        self.q = []  # append, pop(0)

    def push(self, x: int) -> None:
        """
        Time: O(n)
        """
        self.q.append(x)
        n = len(self.q)
        while n > 1:
            self.q.append(self.q.pop(0))
            n -= 1

    def pop(self) -> int:
        """
        Time: O(1) # amortized
        """
        return self.q.pop(0)

    def top(self) -> int:
        """
        Time: O(1)
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Time: O(1)
        """
        return len(self.q) == 0
