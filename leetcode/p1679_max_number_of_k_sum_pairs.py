from typing import List
from collections import defaultdict


def maxOperations(nums: List[int], k: int) -> int:
    prev = defaultdict(int)
    max_ops = 0
    for n in nums:
        if k - n in prev and prev[k - n] != 0:
            max_ops += 1
            prev[k - n] = prev[k - n] - 1
        else:
            prev[n] = prev[n] + 1
    return max_ops
