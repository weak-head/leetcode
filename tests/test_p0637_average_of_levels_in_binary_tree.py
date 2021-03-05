# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p0637_average_of_levels_in_binary_tree import *

solutions = [
    averageOfLevels_bfs,
    averageOfLevels_dfs,
]

test_cases = [
    ([3, 9, 20, 15, 7], [3, 14.5, 11]),
    ([1], [1]),
    ([1, 1, 1, 1, 1, 1, 1], [1, 1, 1]),
    ([1, 2, 2, 3, 3, 3, 3, 4], [1, 2, 3, 4]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(tree(args)) == expectation


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
