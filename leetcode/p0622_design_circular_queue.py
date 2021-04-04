class MyCircularQueue:
    """
    Cyclic array,
    All operations are O(1)
    """

    def __init__(self, k: int):
        self.q = [None] * k
        self.rear = 0
        self.front = 0
        self.n = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.n
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.front] = None
        self.front = (self.front + 1) % self.n
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.rear - 1) % self.n]

    def isEmpty(self) -> bool:
        return self.q[self.front] is None

    def isFull(self) -> bool:
        return self.q[self.rear] is not None
