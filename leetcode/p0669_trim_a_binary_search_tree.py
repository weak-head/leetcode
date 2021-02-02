class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def trimBST(root: TreeNode, low: int, high: int) -> TreeNode:
    """
    Having boundary of the tree,
    we can drop tree nodes moving down.

    Time: O(n)
    Space: O(n) # call stack
        n - number of nodes in the tree
    """

    def trim(node):
        if not node:
            return None

        elif node.val > high:
            return trim(node.left)
        elif node.val < low:
            return trim(node.right)
        else:
            node.left = trim(node.left)
            node.right = trim(node.right)
            return node

    return trim(root)
