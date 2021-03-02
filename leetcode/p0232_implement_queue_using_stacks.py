class MyQueue:
    def __init__(self):
        self.s1 = []  # append, pop
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        """
        Time: O(n) # worst case
        Time: O(1) # amortized
        """
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        """
        Time: O(n) # worst case
        Time: O(1) # amortized
        """
        if not self.s2:
            while self.s1:
                v = self.s1.pop()
                self.s2.append(v)
        return self.s2[-1]

    def empty(self) -> bool:
        return not (self.s1 or self.s2)
