from typing import List
from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verticalOrder(root: TreeNode) -> List[List[int]]:
    """
    BFS guarantees that we have correct column order
    O(n)
    """
    if not root:
        return []

    rows = defaultdict(list)
    min_row, max_row = 0, 0

    q = deque([(root, 0)])
    while q:
        node, crow = q.pop()
        min_row = min(min_row, crow)
        max_row = max(max_row, crow)

        rows[crow].append(node.val)

        if node.left:
            q.appendleft((node.left, crow - 1))

        if node.right:
            q.appendleft((node.right, crow + 1))

    # instead of sort(), so we have O(n), but not O(n * log(n))
    return [rows[ix] for ix in range(min_row, max_row + 1)]
