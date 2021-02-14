class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: TreeNode) -> bool:
    """
    Time: O(n)
    Space: O(h)
        n - number of nodes
        h - height of the tree
    """
    if not root:
        return True

    def is_symmetric(n1, n2):
        if n1 is None and n2 is None:
            return True

        if not (n1 and n2):
            return False

        if n1.val != n2.val:
            return False

        return is_symmetric(n1.left, n2.right) and is_symmetric(n1.right, n2.left)

    return is_symmetric(root.left, root.right)
