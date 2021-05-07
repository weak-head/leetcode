from math import log
from typing import List


def powerfulIntegers(x: int, y: int, bound: int) -> List[int]:
    """
    x^i + y^j <= bound

    Time: O(n * m)
    Space: O(n * m)
        n - log x bound
        m - log y bound
    """

    a = bound if x == 1 else int(log(bound, x))
    b = bound if y == 1 else int(log(bound, y))

    powerful_integers = set()

    for i in range(a + 1):
        for j in range(b + 1):

            value = x ** i + y ** j

            if value <= bound:
                powerful_integers.add(value)

            if y == 1:
                break

        if x == 1:
            break

    return list(powerful_integers)
