class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxProduct(root) -> int:
    """
    Time: O(n)
    Space: O(n)
        n - number of nodes in the tree
    """

    if not root:
        return 0

    ps = []

    def tsum(node):
        if node is None:
            return 0

        s = tsum(node.left) + tsum(node.right) + node.val
        ps.append(s)
        return s

    s = tsum(root)
    median = int(s / 2)

    best = float("inf")
    for v in ps:
        if abs(median - best) > abs(median - v):
            best = v

    return (best * (s - best)) % (10 ** 9 + 7)
