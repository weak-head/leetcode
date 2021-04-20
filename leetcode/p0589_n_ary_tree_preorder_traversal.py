from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def preorder(root: "Node") -> List[int]:
    """
    Time: O(n)
    Space: O(h)
        n - number of nodes in the tree
        h - max height of the tree
    """

    res = []

    def traverse(node):
        nonlocal res

        if node is None:
            return

        res.append(node.val)
        for child in node.children:
            traverse(child)

    traverse(root)
    return res
