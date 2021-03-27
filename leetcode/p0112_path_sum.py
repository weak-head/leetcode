class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    """
    Time: O(n)
    Space: O(h)
        n - number of nodes
        h - max height of the tree
    """
    if root is None:
        return False

    if root.left is None and root.right is None and root.val == targetSum:
        return True

    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(
        root.right, targetSum - root.val
    )
