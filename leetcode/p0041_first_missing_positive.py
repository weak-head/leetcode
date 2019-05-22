from typing import List


def firstMissingPositive(nums: List[int]) -> int:
    if not nums:
        return 1

    nums_len = len(nums)

    # We can use indexes of the array to track
    # the existence of each positive element.
    # So our goal is to swap all elements of the array
    # to the appropriate indexes, ignoring elements that are
    # outside the array or less than 1.
    # We are shifting all elements by one index left,
    # to simplify the calculations:
    #  - 1 should have index 0
    #  - 2 should have index 1
    for ix in range(0, nums_len):
        while nums[ix] > 0 and nums[ix] < nums_len and nums[ix] != nums[nums[ix] - 1]:
            nums[nums[ix] - 1], nums[ix] = nums[ix], nums[nums[ix] - 1]

    # Comparing the value with the index
    # we can find the missing element
    for ix in range(nums_len):
        if nums[ix] != ix + 1:
            return ix + 1

    return nums_len + 1
