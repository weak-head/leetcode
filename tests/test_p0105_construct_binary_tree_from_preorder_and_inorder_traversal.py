# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p0105_construct_binary_tree_from_preorder_and_inorder_traversal import *

solutions = [
    buildTree,
    buildTree_quadratic,
]

#   ([args], expectation),
test_cases = [
    ([3, 9, 20, None, None, 15, 7]),
    ([1, None, 2, None, 3, 5, 7, 9, 11, 12, 13, None, 14, None, None, None, 15]),
    ([1, 2, 3]),
    ([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8]),
    ([1, None, 3, 5, 6, 7, 8, None, None, None, 9, None, 10]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, solution):
    inorder, preorder = [], []
    traverse(tree(args), preorder, inorder)
    assert array(solution(preorder, inorder)) == args


def traverse(node, preorder, inorder):
    if node is None:
        return

    preorder.append(node.val)

    if node.left:
        traverse(node.left, preorder, inorder)

    inorder.append(node.val)

    if node.right:
        traverse(node.right, preorder, inorder)


def tree(a):
    if not a:
        return None

    root, ix = TreeNode(a[0]), 1
    q = deque([root])
    while q and ix < len(a):
        node = q.popleft()

        if ix < len(a) and a[ix] is not None:
            node.left = TreeNode(a[ix])
            q.append(node.left)
        ix += 1

        if ix < len(a) and a[ix] is not None:
            node.right = TreeNode(a[ix])
            q.append(node.right)
        ix += 1

    return root


def array(t):
    if not t:
        return []

    res = [t.val]
    q = deque([t])
    while q:
        node = q.popleft()

        if node.left:
            res.append(node.left.val)
            q.append(node.left)
        else:
            res.append(None)

        if node.right:
            res.append(node.right.val)
            q.append(node.right)
        else:
            res.append(None)

    # Drop redundant None elements from right
    while res[-1] is None:
        res.pop()

    return res
