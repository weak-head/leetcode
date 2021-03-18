from typing import List


def wiggleMaxLength_dp_optimized_space_time(nums: List[int]) -> int:
    """
    Space and time optimized dynamic programming

    Time: O(n)
    Space: O(1)
    """
    up = down = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            up = down + 1
        elif nums[i] < nums[i - 1]:
            down = up + 1
    return max(up, down)


def wiggleMaxLength_dp_optimized(nums: List[int]) -> int:
    """
    Time optimized dynamic programming

    Time: O(n)
    Space: O(n)
    """
    m = [(1, 1)] * len(nums)  # (wiggle down, wiggle up)
    max_len = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:  # move up
            down = m[i - 1][0]
            up = m[i - 1][0] + 1
            m[i] = (down, up)
        elif nums[i] < nums[i - 1]:  # move down
            down = m[i - 1][1] + 1
            up = m[i - 1][1]
            m[i] = (down, up)
        else:
            m[i] = m[i - 1]
        max_len = max(max_len, m[i][0], m[i][1])
    return max_len


def wiggleMaxLength_dp(nums: List[int]) -> int:
    """
    Dynamic programming

    Similar to:
        - house robber
        - stone game
        - buy/sell stocks

    For each number we track two states:
        - length when the previous value is smaller
        - length when the previous value is greater

    Time: O(n^2)
    Space: O(n)
        n - length of the array
    """
    m = [(1, 1)] * len(nums)  # (smaller, greater)
    max_len = 1

    for i in range(1, len(nums)):

        smaller = greater = 1
        for j in range(i):
            if nums[j] < nums[i]:
                smaller = max(smaller, m[j][1] + 1)
            elif nums[j] > nums[i]:
                greater = max(greater, m[j][0] + 1)

        m[i] = (smaller, greater)
        max_len = max(max_len, smaller, greater)

    return max_len
