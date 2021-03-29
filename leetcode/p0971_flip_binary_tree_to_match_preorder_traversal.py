from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flipMatchVoyage(root: TreeNode, voyage: List[int]) -> List[int]:
    """
    Pre-order traversal
    """
    i = 0
    flips = []

    def traverse(node):
        nonlocal i, flips

        if node is None:
            return

        if node.val != voyage[i]:
            flips = [-1]
            return

        i += 1

        if i < len(voyage) and node.left and node.left.val != voyage[i]:
            flips.append(node.val)
            traverse(node.right)
            traverse(node.left)
        else:
            traverse(node.left)
            traverse(node.right)

    traverse(root)
    if flips and flips[0] == -1:
        return [-1]
    return flips
