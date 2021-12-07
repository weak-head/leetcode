from typing import List


def minCostToMoveChips(position: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
        n - number of chips
    """
    even_cnt = odd_cnt = 0
    for chip in position:
        if chip % 2 == 0:
            even_cnt += 1
        else:
            odd_cnt += 1
    return min(even_cnt, odd_cnt)
