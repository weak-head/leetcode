class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def addOneRow(root: TreeNode, v: int, d: int) -> TreeNode:
    if not root:
        return

    if d == 1:
        return TreeNode(v, left=root)

    def insert(node, h):
        if not node:
            return

        if h == d - 1:
            l = node.left
            r = node.right
            node.left = TreeNode(v, left=l)
            node.right = TreeNode(v, right=r)
        else:
            insert(node.left, h + 1)
            insert(node.right, h + 1)

    insert(root, 1)
    return root
