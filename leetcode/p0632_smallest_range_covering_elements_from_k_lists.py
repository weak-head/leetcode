from typing import List
import heapq


def smallestRange(nums: List[List[int]]) -> List[int]:
    """
    Time: O(n * log m)
    Space: O(m)
        n - number of lists
        m - max length of the list
    """

    # (number, list_index, number_index)
    pq = [(row[0], i, 0) for i, row in enumerate(nums)]

    heapq.heapify(pq)

    ans = -1e9, 1e9
    right = max(row[0] for row in nums)

    while pq:
        # number, list_index, number_index
        left, i, j = heapq.heappop(pq)

        # adjust range, if it is smaller
        if right - left < ans[1] - ans[0]:
            ans = left, right

        # reached the end of the list
        # the answer cannot be smaller
        if j + 1 == len(nums[i]):
            return ans

        v = nums[i][j + 1]
        right = max(right, v)

        heapq.heappush(pq, (v, i, j + 1))
