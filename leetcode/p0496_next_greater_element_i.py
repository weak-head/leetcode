from typing import List


def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Monotonic stack

    Time: O(n)
    Space: O(n)
    """
    s = []
    r = {}
    for i in range(len(nums2) - 1, -1, -1):
        while s and nums2[s[-1]] <= nums2[i]:
            s.pop()

        next_greater = -1 if not s else nums2[s[-1]]
        r[nums2[i]] = next_greater
        s.append(i)

    return [r[n] for n in nums1]
