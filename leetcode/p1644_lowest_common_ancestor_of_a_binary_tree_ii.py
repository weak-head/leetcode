class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
    """
    Time: O(n)
    Space: O(h)
        n - number of nodes in the tree
        h - max height of the tree
    """

    lca = None

    def find(node):
        nonlocal lca
        if node is None:
            return False

        left = find(node.left)
        right = find(node.right)

        p_or_q = (node == p) or (node == q)

        if (left and right) or (left and p_or_q) or (right and p_or_q):
            lca = node

        return left or right or p_or_q

    find(root)
    return lca
