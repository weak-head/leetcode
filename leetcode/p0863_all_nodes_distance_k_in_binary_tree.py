from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def distanceK(root: TreeNode, target: TreeNode, k: int) -> List[int]:
    """
    Time: O(n)
    Space: O(n)
    """

    if root is None or target is None:
        return []

    # annotate
    def dfs(node, par=None):
        if node is not None:
            node.par = par
            dfs(node.left, node)
            dfs(node.right, node)

    dfs(root)

    seen = {target}
    res = []
    q = deque([(target, 0)])

    while q:
        node, distance = q.popleft()

        if distance == k:
            res.append(node.val)
        else:
            if node.par is not None and node.par not in seen:
                seen.add(node.par)
                q.append((node.par, distance + 1))

            if node.left is not None and node.left not in seen:
                seen.add(node.left)
                q.append((node.left, distance + 1))

            if node.right is not None and node.right not in seen:
                seen.add(node.right)
                q.append((node.right, distance + 1))

    return res
