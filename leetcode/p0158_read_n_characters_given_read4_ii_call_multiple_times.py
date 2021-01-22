from typing import List
from collections import deque


def read4(b):
    b[0] = "a"
    b[1] = "b"
    b[2] = "c"
    b[3] = "d"
    return 4


class Solution:
    def __init__(self):
        self.q = deque()

    def read(self, buf: List[str], n: int) -> int:
        """"""
        i = 0
        while i < n:
            if self.q:
                buf[i] = self.q.pop()
                i += 1
            else:
                buf4 = [""] * 4
                rn = read4(buf4)

                if not rn:
                    break

                for ix in range(rn):
                    self.q.appendleft(buf4[ix])
        return i
