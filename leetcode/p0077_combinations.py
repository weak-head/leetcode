from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    """
    Backtracking

    Time: O( k * (n! / ((n-k)! * k!)) )
    Space: O(n! / ((n-k)! * k!))
    """

    res = []

    def track(start, combination):
        if len(combination) == k:
            res.append(list(combination))  # O(k)
            return

        for i in range(start, n + 1):
            combination.append(i)
            track(i + 1, combination)
            combination.pop()

    track(1, [])
    return res
