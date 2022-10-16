from typing import List


def lemonadeChange(bills: List[int]) -> bool:
    """
    Time: O(n)
    Space: O(1)
    """

    c5 = c10 = 0

    for bill in bills:
        if bill == 5:
            c5 += 1

        elif bill == 10:
            if c5 == 0:
                return False
            else:
                c5 -= 1
                c10 += 1

        elif bill == 20:
            if c5 != 0 and c10 != 0:
                c5 -= 1
                c10 -= 1
            elif c5 >= 3:
                c5 -= 3
            else:
                return False

    return True
