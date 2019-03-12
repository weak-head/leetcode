from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n * log n)
def bstFromPreorder2(preorder: List[int]) -> TreeNode:
    root = TreeNode(preorder[0])
    for x in range(1, len(preorder)):
        insert(root, preorder[x])
    return root

def insert(node: TreeNode, x: int) -> TreeNode:
    if node is None:
        return TreeNode(x)
    elif x < node.val:
        node.left = insert(node.left, x)
    else:
        node.right = insert(node.right, x)
    return node

# O(n)
def bstFromPreorder(preorder: List[int]) -> TreeNode:
    stack, root = [], TreeNode(preorder[0])
    ix, node = 1, root
    while ix < len(preorder):
        el = preorder[ix]
        if el < node.val:
            stack.append(node)
            node.left = TreeNode(el)
            node = node.left
            ix = ix + 1
        else:
            if len(stack) == 0:
                node.right = TreeNode(el)
                node = node.right
                ix = ix + 1
            elif stack[-1].val > el:
                node.right = TreeNode(el)
                node = node.right
                ix = ix + 1
            else:
                node = stack.pop()
    return root