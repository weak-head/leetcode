from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def verticalTraversal(root: TreeNode) -> List[List[int]]:
    od = {}
    traverse(root, 0, 0, od)

    res = []
    for _, v in sorted(od.items()):
        sv = sorted(v)
        val = list(map(lambda k: k[1], sv))
        res.append(val)

    return res


def traverse(node, ix, iy, od):
    if node is None:
        return

    traverse(node.left, ix - 1, iy + 1, od)

    if ix not in od:
        od[ix] = []
    od[ix].append((iy, node.val))

    traverse(node.right, ix + 1, iy + 1, od)
