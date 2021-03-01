from collections import Counter
from typing import List


def distributeCandies(candyType: List[int]) -> int:
    """
    Time: O(n)
    Space: O(n)
        n - length of array
    """
    can_eat = len(candyType) // 2
    max_types = len(Counter(candyType))
    return min(can_eat, max_types)
