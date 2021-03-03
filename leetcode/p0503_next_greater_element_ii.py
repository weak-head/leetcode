from typing import List


def nextGreaterElements(nums: List[int]) -> List[int]:
    """
    Monotonic stack

    Time: O(n)
    Space: O(n)
    """
    n = len(nums)
    s = []
    r = [None] * n

    for i in range(2 * (n - 1), -1, -1):
        while s and nums[s[-1] % n] <= nums[i % n]:
            s.pop()

        next_greater = -1 if not s else nums[s[-1] % n]
        r[i % n] = next_greater
        s.append(i)

    return r
