from typing import List
from bisect import bisect_left


def length_of_lis_dp_bs(nums: List[int]) -> int:
    """
    Dynamic Programming + Binary Search + Patience sort

    Video:
        https://www.youtube.com/watch?v=22s1xxRvy28

    Time: O(n * log n)
    Space: O(n)
        n - number of elements in the array
    """

    piles = [0] * len(nums)
    num_piles = 0

    for num in nums:
        dest_pile = bisect_left(piles, num, 0, num_piles)
        if dest_pile == -1:
            dest_pile = 0

        piles[dest_pile] = num
        if dest_pile == num_piles:
            num_piles += 1

    return num_piles


def length_of_lis_dp(nums: List[int]) -> int:
    """
    Classical Dynamic Programming

    Time: O(n * n)
    Space: O(n)
        n - number of elements in the array
    """
    m = [1] * len(nums)
    lis = 1
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                m[i] = max(m[i], m[j] + 1)
                lis = max(m[i], lis)

    return lis
