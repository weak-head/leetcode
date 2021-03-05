from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    """
    Backtracking

    Time: O( k * (n! / ((n-k)! * k!)) )
    Space: O(n! / ((n-k)! * k!))
    """

    res = []
    nums = list(range(1, n + 1))

    def track(start, combination):
        if len(combination) == k:
            res.append(list(combination))  # O(k)
            return

        for i in range(start, len(nums)):
            combination.append(nums[i])
            track(i + 1, combination)
            combination.pop()

    track(0, [])
    return res
