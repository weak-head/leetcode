# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p0285_inorder_successor_in_bst import *

solutions = [
    inorderSuccessor,
]

test_cases = [
    ([[2, 1, 3], 1], 2),
    ([[5, 3, 6, 2, 4, None, None, 1], 6], None),
    ([[2], 2], None),
    ([[2, 1, 4, None, None, 3, 5], 3], 4),
    ([[2, 1, 4, None, None, 3, 5], 4], 5),
    ([[2, 1, 4, None, None, 3, 5], 2], 3),
    ([[2, 1, 4, None, None, 3, 5], 5], None),
    ([[2, 1, 4, None, None, 3, 5], 1], 2),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    root, p = tree(*args)
    node = solution(root, p)
    if expectation is None:
        assert node is None
    else:
        assert node.val == expectation


def tree(a, v):
    root = TreeNode(a[0])
    p = None
    q = deque([root])
    i = 1
    while q:
        node = q.popleft()

        if node.val == v:
            p = node

        if i < len(a) and a[i] is not None:
            node.left = TreeNode(a[i])
            q.append(node.left)
        i += 1

        if i < len(a) and a[i] is not None:
            node.right = TreeNode(a[i])
            q.append(node.right)
        i += 1
    return root, p
