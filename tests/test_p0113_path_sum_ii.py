# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p0113_path_sum_ii import *

solutions = [
    pathSum,
]

test_cases = [
    (
        [[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22],
        [[5, 4, 11, 2], [5, 8, 4, 5]],
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    a, v = args
    assert solution(tree(a), v) == expectation


def tree(a):
    root = TreeNode(a[0])
    i = 1
    q = deque([root])

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
