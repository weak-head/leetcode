from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root: "TreeNode", nodes: "List[TreeNode]") -> "TreeNode":
    """
    Time: O(n)
    Space: O(m + h)
        n - number of nodes in the tree
        m - number of nodes in the list
        h - max height of the tree
    """
    state = set(nodes)
    lca = None

    def find(node: TreeNode):
        nonlocal lca, state
        if node is None:
            return False

        drop_this = False
        if node in state:
            state.remove(node)
            drop_this = True

        drop_left = find(node.left)
        drop_right = find(node.right)

        if not state:
            if drop_this or (drop_left and drop_right):
                lca = node

        return drop_right or drop_left or drop_this

    find(root)
    return lca


def lowestCommonAncestor_optimized(
    root: "TreeNode", nodes: "List[TreeNode]"
) -> "TreeNode":
    """
    This solution is similar to the previous,
    but we avoid removing elements from the set,
    and it makes the time constant next to O(n) a little
    bit smaller.

    Also this solution is optimistic,
    if 'root' in nodes, we avoid checking
    left and right children.

    Time: O(n)
    Space: O(m + h)
        n - number of nodes in the tree
        m - number of nodes in the list
        h - max height of the tree
    """
    nodes = set(nodes)

    def find(root):
        nonlocal nodes
        if not root:
            return None

        if root in nodes:
            return root

        l = find(root.left)
        r = find(root.right)

        if l and r:
            return root

        if l or r:
            return l or r

    return find(root)
