class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def treeToDoublyList(root: "Node") -> "Node":
    """
    Time:
    O(n)
    n - number of nodes in the tree

    Space:
    O(n)      - unbalanced
    O(log(n)) - balanced
    """
    if not root:
        return None

    def inOrder(node: Node) -> (Node, Node):
        if not node:
            return None, None

        l_first, l_last = inOrder(node.left)
        if l_last:
            l_last.right = node
            node.left = l_last
        if not l_first:
            l_first = node

        r_first, r_last = inOrder(node.right)
        if r_first:
            node.right = r_first
            r_first.left = node
        if not r_last:
            r_last = node

        return l_first, r_last

    first, last = inOrder(root)
    first.left = last
    last.right = first

    return first
