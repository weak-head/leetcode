from typing import Tuple


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
    Space: O(k)
        n - number of houses/nodes
        k - max depth of the tree
    """

    def rob_node(node: TreeNode) -> Tuple[int, int]:
        if not node:
            return (0, 0)  # (if_skip, if_rob)

        left = rob_node(node.left)
        right = rob_node(node.right)

        # if we rob this house, we have to skip both children
        if_rob = node.val + left[0] + right[0]

        # if we skip this house, we can rob or skip both children
        if_skip = max(left) + max(right)

        return (if_skip, if_rob)

    return max(rob_node(root))
