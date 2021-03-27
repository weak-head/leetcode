from typing import List


def pathSum(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(n)
        n - number of nodes in the tree
    """
    m = {v // 10: v % 10 for v in nums}
    total = 0

    def traverse(node, total_sum):
        nonlocal total, m
        if node not in m:
            return

        total_sum += m[node]

        depth, pos = divmod(node, 10)
        left = (depth + 1) * 10 + 2 * pos - 1
        right = left + 1

        if left not in m and right not in m:
            total += total_sum
        else:
            traverse(left, total_sum)
            traverse(right, total_sum)

    traverse(nums[0] // 10, 0)
    return total
