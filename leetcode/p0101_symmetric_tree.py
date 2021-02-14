from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric_recursive(root: TreeNode) -> bool:
    """
    Time: O(n)
    Space: O(h)
        n - number of nodes
        h - height of the tree
    """
    if not root:
        return True

    def is_symmetric(n1, n2):
        if n1 is None and n2 is None:
            return True

        if not (n1 and n2):
            return False

        if n1.val != n2.val:
            return False

        return is_symmetric(n1.left, n2.right) and is_symmetric(n1.right, n2.left)

    return is_symmetric(root.left, root.right)


def isSymmetric_iterative(root: TreeNode) -> bool:
    """
    In the worst case, when the tree is full,
    we would have to insert the entire bottom level,
    that has effectively (n // 2) elements.

    Time: O(n)
    Space: (n)
        n - number of elements in the tree
    """
    if not root:
        return True

    q = deque([(root.left, root.right)])
    while q:
        a, b = q.popleft()

        if a is None and b is None:
            continue

        if not (a and b):
            return False

        if a.val != b.val:
            return False

        q.append((a.left, b.right))
        q.append((a.right, b.left))

    return True
