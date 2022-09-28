from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Time: O(n)
    Space: O(n)
    """
    if root is None:
        return []

    q = deque([(root, 0)])
    r = []

    while q:
        node, level = q.popleft()

        if level >= len(r):
            r.append(deque())

        if level % 2 == 0:
            r[level].append(node.val)
        else:
            r[level].appendleft(node.val)

        if node.left is not None:
            q.append((node.left, level + 1))
        if node.right is not None:
            q.append((node.right, level + 1))

    return r
