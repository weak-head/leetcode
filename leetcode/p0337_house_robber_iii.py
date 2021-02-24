from typing import Tuple
from functools import lru_cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rob(root: TreeNode) -> int:
    """
    Dynamic Programming
    Similar to:
        - 198 https://leetcode.com/problems/house-robber/
        - 213 https://leetcode.com/problems/house-robber-ii/

    Time: O(n)
    Space: O(n)
        n - number of houses/nodes
    """

    @lru_cache(None)
    def rob_node(node: TreeNode) -> Tuple[int, int]:
        if not node:
            return (0, 0)

        # if we rob this house, we have to skip both children
        if_rob = node.val + rob_node(node.left)[0] + rob_node(node.right)[0]

        # if we skip this house, we can rob or skip both children
        if_skip = max(rob_node(node.left)) + max(rob_node(node.right))

        return (if_skip, if_rob)

    return max(rob_node(root))
