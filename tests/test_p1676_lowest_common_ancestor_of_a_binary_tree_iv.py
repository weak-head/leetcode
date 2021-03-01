# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p1676_lowest_common_ancestor_of_a_binary_tree_iv import *

solutions = [
    lowestCommonAncestor,
    lowestCommonAncestor_optimized,
]

test_cases = [
    ([[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], [4, 7]], 2),
    ([[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], [1]], 1),
    ([[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], [7, 6, 2, 4]], 5),
    ([[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], [0, 1, 2, 3, 4, 5, 6, 7, 8]], 3),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*tree(*args)).val == expectation


def tree(a, s):
    root = TreeNode(a[0])
    i = 1
    q = deque([root])
    r = []
    while q:
        node = q.popleft()

        if node.val in s:
            r.append(node)

        if i < len(a) and a[i] is not None:
            left = TreeNode(a[i])
            node.left = left
            q.append(left)
        i += 1

        if i < len(a) and a[i] is not None:
            right = TreeNode(a[i])
            node.right = right
            q.append(right)
        i += 1

    return root, r
