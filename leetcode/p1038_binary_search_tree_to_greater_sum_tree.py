class TreeNode:
    def __init__(self, v=0, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r


def convertBST(root: TreeNode) -> TreeNode:
    """
    Time: O(n)
    Space: O(1)
        n - number of nodes in the tree
    """

    def conv(node: TreeNode, greater_sum) -> int:
        """
        Reverse in-order (RNL) traversal
        https://en.wikipedia.org/wiki/Tree_traversal
        """
        if node is None:
            return greater_sum

        node.val += conv(node.right, greater_sum)
        return conv(node.left, node.val)

    conv(root, 0)
    return root
