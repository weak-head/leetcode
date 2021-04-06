from typing import List
import heapq
from random import randint


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

    def partition(i, j) -> int:
        index = randint(i, j)
        nums[index], nums[j] = nums[j], nums[index]

        for k in range(i, j):
            if nums[k] <= nums[j]:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1

        nums[i], nums[j] = nums[j], nums[i]
        return i

    def sort(i, j) -> int:
        pivot = partition(i, j)
        if pivot == pos:
            return nums[pos]
        elif pos < pivot:
            return sort(i, pivot - 1)
        else:
            return sort(pivot + 1, j)

    n = len(nums)
    pos = n - k
    return sort(0, n - 1)
