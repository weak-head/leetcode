from typing import List


def numSubseq(nums: List[int], target: int) -> int:
    """
    Similar to Two Sum,
    Sliding window

    Time: O(n * log(n))
    Space: O(1)
        n - number of elements in the array
    """
    nums.sort()
    cnt, modulus = 0, pow(10, 9) + 7
    left, right = 0, len(nums) - 1
    while left <= right:
        if nums[left] + nums[right] <= target:
            cnt += pow(2, right - left, modulus)
            left += 1
        else:
            right -= 1

    return cnt % modulus
