from typing import List
from collections import defaultdict, deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def verticalTraversal(root: TreeNode) -> List[List[int]]:
    """
    BFS

    Time: O(n * log(n / k))
    Space: O(n)
        n - number of nodes in the tree
        k - width of the tree

    """
    m = defaultdict(list)
    q = deque([(root, 0, 0)])  # val, row, col
    l, r = 0, 0

    while q:
        node, row, col = q.popleft()
        l, r = min(col, l), max(col, r)

        m[col].append((row, node.val))
        if node.left:
            q.append((node.left, row + 1, col - 1))
        if node.right:
            q.append((node.right, row + 1, col + 1))

    result = []
    for col in range(l, r + 1):
        result.append([v for _, v in sorted(m[col])])

    return result
