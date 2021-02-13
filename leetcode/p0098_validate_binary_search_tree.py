class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: TreeNode) -> bool:
    """
    Time: O(n)
    Space: O(h)
        n - number of nodes in the tree
        h - height of the three
    """

    def isValid(node, left, right):
        if node is None:
            return True

        if not (left < node.val < right):
            return False

        if node.left:
            if not isValid(node.left, left, node.val):
                return False

        if node.right:
            return isValid(node.right, node.val, right)

        return True

    return isValid(root, float("-inf"), float("inf"))
