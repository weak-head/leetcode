class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deleteNode(root: TreeNode, key: int) -> TreeNode:
    """
    Time: O(h)
    Space: O(h)
        h - max height of the tree
    """

    def min_node(node):
        while node.left is not None:
            node = node.left
        return node

    def del_node(node, key):
        if node is None:
            return None

        if node.val == key:
            # no children
            if node.left is None and node.right is None:
                return None

            # single child
            if node.left is not None and node.right is None:
                return node.left
            if node.left is None and node.right is not None:
                return node.right

            # two children
            min_n = min_node(node.right)
            node.val = min_n.val
            node.right = del_node(node.right, node.val)

        elif node.val > key:
            node.left = del_node(node.left, key)
        else:
            node.right = del_node(node.right, key)

        return node

    return del_node(root, key)
