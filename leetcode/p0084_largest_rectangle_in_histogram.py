from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    """
    Monotonic stack

    Time: O(n)
    Space: O(n)
        n - length of the array
    """
    stack = []
    res = 0
    heights = [0] + heights + [0]

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            index = stack.pop()
            res = max(res, (i - stack[-1] - 1) * heights[index])

        stack.append(i)

    return res
