# flake8: noqa: F403, F405
import pytest
from leetcode.p0102_binary_tree_level_order_traversal import *
from collections import deque

solutions = [
    levelOrder,
]

test_cases = [
    ([], []),
    ([1], [[1]]),
    ([1, 2, 3], [[1], [2, 3]]),
    ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(tree(args)) == expectation


def tree(a):
    if not a:
        return None

    root = TreeNode(a[0])
    q = deque([root])
    i = 1

    while q:
        node = q.popleft()

        if i < len(a) and a[i] is not None:
            node.left = TreeNode(a[i])
            q.append(node.left)
        i += 1

        if i < len(a) and a[i] is not None:
            node.right = TreeNode(a[i])
            q.append(node.right)
        i += 1

    return root
