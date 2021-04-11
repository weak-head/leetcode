from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deepestLeavesSum(root: TreeNode) -> int:
    """
    DFS with hashtable

    Time: O(n)
    Space: O(h)
    """
    r = defaultdict(int)

    def dfs(node, depth):
        if node is None:
            return

        r[depth] += node.val
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 1)
    return r[len(r)]
