from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root: TreeNode, targetSum: int) -> List[List[int]]:
    """
    Time: O(n)
    Space: O(h)
        n - number of nodes
        h - max height of the tree
    """

    res = []

    def preorder(node, path, s):
        if node is None:
            return

        if node.left is None and node.right is None and node.val == s:
            res.append(path + [node.val])

        preorder(node.left, path + [node.val], s - node.val)
        preorder(node.right, path + [node.val], s - node.val)

    preorder(root, [], targetSum)
    return res
