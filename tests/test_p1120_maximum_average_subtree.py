# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p1120_maximum_average_subtree import *

solutions = [
    maximumAverageSubtree,
]

test_cases = [
    ([5, 6, 1], 6),
    ([0, None, 1], 1),
    ([2, 3, 5, 2, 3, 5, 6, 4, 2, 3, 6], 6),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(to_tree(args)) == expectation


def to_tree(a):
    root = TreeNode(val=a[0])
    q = deque([root])
    i = 1
    while q and i < len(a):
        node = q.popleft()

        if i < len(a) and a[i] is not None:
            node.left = TreeNode(val=a[i])
            q.append(node.left)
        i += 1

        if i < len(a) and a[i] is not None:
            node.right = TreeNode(val=a[i])
            q.append(node.right)
        i += 1
    return root
