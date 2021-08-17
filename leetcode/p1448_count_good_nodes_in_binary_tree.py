class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def goodNodes(root: TreeNode) -> int:
    """
    Space: O(n)
    Time: O(n)
        n - number of nodes in the tree
    """

    def good(node, max_val):
        if not node:
            return 0

        mv = max(node.val, max_val)
        c = 1 if node.val >= max_val else 0

        lc = good(node.left, mv)
        rc = good(node.right, mv)

        return c + lc + rc

    return good(root, float("-inf"))
