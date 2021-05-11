from typing import List


def maxScore_sliding_window(cardPoints: List[int], k: int) -> int:
    """
    Sliding window

    Time: O(n)
    Space: O(1)
        n - number of elements
    """
    size = len(cardPoints) - k
    min_sum = cur_sum = sum(cardPoints[:size])

    for i in range(size, len(cardPoints)):
        cur_sum += cardPoints[i] - cardPoints[i - size]
        min_sum = min(min_sum, cur_sum)

    return sum(cardPoints) - min_sum


def maxScore_dp(cardPoints: List[int], k: int) -> int:
    """
    Dynamic programming

    Time:
    Space:
    """
    pass
