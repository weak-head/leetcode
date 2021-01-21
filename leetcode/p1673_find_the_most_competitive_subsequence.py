from typing import List


def mostCompetitive(nums: List[int], k: int) -> List[int]:
    """
    Greedy
    Time: O(n)
    Space: O(n)
    """
    q = []

    # From left to right
    for ix, v in enumerate(nums):

        # Try to keep only the smallest elements in queue
        # until it's not longer possible to reduce the queue
        while q and q[-1] > v and (len(nums) - ix) + len(q) > k:
            q.pop()

        q.append(v)

    return q[:k]
