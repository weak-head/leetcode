from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root: TreeNode) -> List[int]:
    """
    Time: O(n)
    Space: O(n)
    """
    r = []

    def walk(node, d):
        if not node:
            return

        if d == len(r):
            r.append(node.val)

        walk(node.right, d + 1)
        walk(node.left, d + 1)

    walk(root, 0)
    return r
