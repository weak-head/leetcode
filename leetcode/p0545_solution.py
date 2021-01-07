from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def boundaryOfBinaryTree1(root: TreeNode) -> List[int]:
    """
    O(n)
    n - number of nodes in the tree
    """

    left_boundary = deque()
    right_boundary = deque()
    leaves = deque()

    class Rel:
        root = 0
        leftBoundary = 1
        rightBoundary = 2
        other = 3

    def isLeaf(node):
        return not (node.left or node.right)

    def flagLeft(node: TreeNode, relation: Rel):
        if (relation == Rel.root) or (relation == Rel.leftBoundary):
            return Rel.leftBoundary
        elif (relation == Rel.rightBoundary) and (not node.right):
            return Rel.rightBoundary
        return Rel.other

    def flagRight(node: TreeNode, relation: Rel):
        if (relation == Rel.root) or (relation == Rel.rightBoundary):
            return Rel.rightBoundary
        elif (relation == Rel.leftBoundary) and (not node.left):
            return Rel.leftBoundary
        return Rel.other

    def preOrder(node: TreeNode, relation: Rel):
        if not node:
            return

        if relation == Rel.rightBoundary:
            right_boundary.appendleft(node.val)
        elif relation == Rel.root or relation == Rel.leftBoundary:
            left_boundary.append(node.val)
        elif isLeaf(node):
            leaves.append(node.val)

        preOrder(node.left, flagLeft(node, relation))
        preOrder(node.right, flagRight(node, relation))

    preOrder(root, Rel.root)
    left_boundary.extend(leaves)
    left_boundary.extend(right_boundary)

    return left_boundary


def boundaryOfBinaryTree2(root):
    """
    O(n)
    n - number of nodes in the tree
    """
    if not root:
        return []

    boundary = [root.val]

    def dfs(root, isleft, isright):
        if root:
            # append when going down from the left or at leaf node
            if (not root.left and not root.right) or isleft:
                boundary.append(root.val)

            if root.left and root.right:
                dfs(root.left, isleft, False)
                dfs(root.right, False, isright)
            else:
                dfs(root.left, isleft, isright)
                dfs(root.right, isleft, isright)

            # append to boundary when coming up from the right
            if (root.left or root.right) and isright:
                boundary.append(root.val)

    dfs(root.left, True, False)
    dfs(root.right, False, True)
    return boundary
