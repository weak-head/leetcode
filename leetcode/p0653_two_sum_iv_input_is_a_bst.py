class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findTarget(root, k):
    """
    Tree travesal

    Time: O(n)
    Space: O(n)
    """

    h = set()

    def traverse(node):
        if not node:
            return False

        if node.val in h:
            return True

        h.add(k - node.val)

        return traverse(node.left) or traverse(node.right)

    return traverse(root)
