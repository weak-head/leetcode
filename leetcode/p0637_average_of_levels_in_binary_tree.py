from typing import List
from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def averageOfLevels_bfs(root: TreeNode) -> List[float]:
    """
    BFS, with small optimization to process level-by-level

    Time: O(n)
    Space: O(w)
        n - number of nodes
        w - width of the tree
    """
    if root is None:
        return []

    r = []
    q = deque([root])
    while q:
        cnt = len(q)  # number of nodes on this level
        s, c = 0, cnt
        while cnt > 0:  # process level-by-level
            cnt -= 1
            node = q.popleft()
            s += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        r.append(s / c)
    return r


def averageOfLevels_dfs(root: TreeNode) -> List[float]:
    """
    DFS

    Time: O(n)
    Space: O(h)
        n - number of nodes
        h - height of the tree
    """

    class Avg:
        def __init__(self):
            self.val = 0
            self.cnt = 0

    l = defaultdict(Avg)
    max_n = 0

    def traverse(node, n):
        nonlocal max_n, l
        if node is None:
            return

        max_n = max(max_n, n)
        avg = l[n]
        avg.val += node.val
        avg.cnt += 1

        traverse(node.left, n + 1)
        traverse(node.right, n + 1)

    traverse(root, 0)

    r = []
    for i in range(max_n + 1):
        avg = l[i].val / l[i].cnt
        r.append(avg)

    return r
