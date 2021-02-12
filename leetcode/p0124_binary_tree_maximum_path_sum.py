import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root: TreeNode) -> int:
    """
    Time: O(n)
    Space: O(h)
        n - number of nodes
        h - max height of the tree
    """

    m = -math.inf

    def maxp(node):
        nonlocal m
        if node is None:
            return 0

        v = node.val
        l, r = maxp(node.left), maxp(node.right)
        m = max(m, v + l + r, v + l, v + r, v)
        return max(v, v + l, v + r)

    maxp(root)
    return m
