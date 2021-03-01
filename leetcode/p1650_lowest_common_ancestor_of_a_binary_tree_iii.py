class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def lowestCommonAncestor(p: "Node", q: "Node") -> "Node":
    """
    Time: O(h)
    Space: O(h)
        h - max length of the tree
    """
    s = set()
    while p is not None:
        s.add(p)
        p = p.parent

    while q is not None:
        if q in s:
            return q
        q = q.parent
