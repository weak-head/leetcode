from typing import List
import heapq


def findKthLargest(nums: List[int], k: int) -> int:
    """
    Time: O(n * log(n))
    Space: O(1)
    """
    heapq.heapify(nums)
    target = len(nums) - k

    while target:
        heapq.heappop(nums)
        target -= 1

    return nums[0]


def findKthLargest2(nums, k):
    """
    Quick Select:
        https://en.wikipedia.org/wiki/Quickselect

    Worst-case: O(n^2)
    Best-case: O(n)
    Average-case: O(n)
    """
    pivot = nums[0]
    left = [l for l in nums if l < pivot]
    equal = [e for e in nums if e == pivot]
    right = [r for r in nums if r > pivot]

    if k <= len(right):
        return findKthLargest2(right, k)
    elif (k - len(right)) <= len(equal):
        return equal[0]
    else:
        return findKthLargest2(left, k - len(right) - len(equal))
