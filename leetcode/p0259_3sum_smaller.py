from typing import List


def threeSumSmaller(nums: List[int], target: int) -> int:
    """
    Sort nums [O(n * log(n))] + two pointers

    Time: O(n ^ 2)
    Space: O(1)
        n - length of the array
    """
    nums.sort()
    c = 0

    # first number
    for left in range(len(nums)):

        # second and third number
        t = target - nums[left]
        l, r = left + 1, len(nums) - 1

        while l < r:
            if nums[l] + nums[r] < t:
                # entire range of indexes between 'l' and 'r'
                c += r - l
                l += 1
            else:
                r -= 1

    return c
