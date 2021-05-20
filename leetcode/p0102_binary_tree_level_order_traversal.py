from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: TreeNode) -> List[List[int]]:
    res = []
    if root is None:
        return res

    q = deque([(root, 1)])
    while q:
        node, level = q.popleft()

        if len(res) < level:
            res.append([])

        res[level - 1].append(node.val)

        if node.left is not None:
            q.append((node.left, level + 1))

        if node.right is not None:
            q.append((node.right, level + 1))

    return res
