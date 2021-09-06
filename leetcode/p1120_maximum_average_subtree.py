from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maximumAverageSubtree(root: Optional[TreeNode]) -> float:
    """
    Time: O(n)
    Space: O(n)
    """
    max_avg = float("-inf")

    def avg(node):
        nonlocal max_avg

        if node is None:
            return (0, 0)

        v1, c1 = avg(node.left)
        v2, c2 = avg(node.right)

        res = (v1 + v2 + node.val, c1 + c2 + 1)
        max_avg = max(max_avg, res[0] / res[1])
        return res

    avg(root)
    return max_avg
