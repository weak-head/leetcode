from typing import List


def search(nums: List[int], target: int) -> int:
    """
    Modified binary search.

    With each iteration we can determine
    if left or right side of the array is rotated.

        - [ 7 8 9 1 |2| 3 4 5 6 ]   (right is not rotated)
        - [ 3 4 5 6 |7| 8 9 1 2 ]   (left is not rotated)

    Then we need to check if |v| is between start and end
    of the not rotated half and based on this make a decision
    of how to adjust start/end of the search range.

    Time: O(log n)
    Space: O(1)
    """
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) >> 1

        if nums[mid] == target:
            return mid

        # left side is not rotated
        if nums[mid] >= nums[start]:
            if target >= nums[start] and target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        # right side is not rotated
        else:
            if target <= nums[end] and target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1

    return -1
