class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorderSuccessor(root: "TreeNode", p: "TreeNode") -> "TreeNode":
    """
    Time: O(n)
    Space: O(h)
        n - number of nodes
        h - max height of the tree
    """
    prev = None
    res = None

    def inorder(node):
        """
        In-order traversal - LNR
        """
        nonlocal prev, res

        if res is not None:
            return

        if node is None:
            return

        # Left child
        inorder(node.left)

        # This node
        if prev == p:
            res = node

        # Previous for "right"
        prev = node

        # Right child
        inorder(node.right)

    inorder(root)
    return res
