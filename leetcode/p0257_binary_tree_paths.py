class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def binaryTreePaths(root: TreeNode):
    stack, res = [], []
    traverse(root, stack, res)
    return res


def traverse(node, stack, res):
    if not node:
        return

    stack.append(str(node.val))

    if not node.left and not node.right:
        res.append("->".join(stack))
    else:
        traverse(node.left, stack, res)
        traverse(node.right, stack, res)

    stack.pop()
