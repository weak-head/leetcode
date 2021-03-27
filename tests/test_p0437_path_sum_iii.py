# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p0437_path_sum_iii import *

solutions = [
    pathSum_bf,
    pathSum_prefix_sum,
]

test_cases = [
    ([[10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8], 3),
    ([[10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 7], 2),
    ([[10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 3], 3),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    a, k = args
    assert solution(tree(a), k) == expectation


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
