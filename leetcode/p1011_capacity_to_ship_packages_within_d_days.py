from typing import List


def shipWithinDays(weights: List[int], D: int) -> int:
    """
    Binary search over the range of [max(weights) : sum(weights)]

    Time: O(n * log n)
    Space: O(n)
    """
    l = r = 0
    for w in weights:
        l = max(l, w)
        r += w

    def can_ship(weight):
        days = 1
        cur_weight = 0
        for w in weights:
            if w + cur_weight <= weight:
                cur_weight += w
            else:
                days += 1
                cur_weight = w
        return days <= D

    while l < r:
        weight = (l + r) // 2
        if can_ship(weight):
            r = weight
        else:
            l = weight + 1

    return r
