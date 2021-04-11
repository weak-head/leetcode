# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p1302_deepest_leaves_sum import *

solutions = [
    deepestLeavesSum,
]

test_cases = [
    ([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8], 15),
    ([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5], 19),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(tree(args)) == expectation


def tree(a):
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
