from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def widthOfBinaryTree(root: Optional[TreeNode]) -> int:
    """
    Depth-first search
    with column tracking

    Time: O(n)
    Space: O(n)
    """

    left_most_index = {}
    max_width = 0

    def dfs(node, depth, column):
        nonlocal max_width
        if node is None:
            return

        # track left-most node on this depth
        if depth not in left_most_index:
            left_most_index[depth] = column

        max_width = max(max_width, column - left_most_index[depth] + 1)

        dfs(node.left, depth + 1, column * 2)
        dfs(node.right, depth + 1, column * 2 + 1)

    dfs(root, 0, 0)
    return max_width
