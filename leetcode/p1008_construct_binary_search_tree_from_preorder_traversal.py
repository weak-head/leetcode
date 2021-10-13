from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bstFromPreorder(preorder: List[int]) -> TreeNode:
    """
    Time: O(n)
    Space: O(n)
        n - number of nodes in the tree
    """
    stack = []
    node = root = TreeNode(preorder[0])
    ix = 1

    while ix < len(preorder):
        el = preorder[ix]

        if el < node.val:
            stack.append(node)
            node.left = TreeNode(el)
            node = node.left
            ix = ix + 1
        else:
            if len(stack) == 0 or stack[-1].val > el:
                node.right = TreeNode(el)
                node = node.right
                ix = ix + 1
            else:
                node = stack.pop()

    return root
