# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p0236_lowest_common_ancestor_of_a_binary_tree import *

solutions = [
    lowestCommonAncestor,
]

test_cases = [
    ([[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1], 3),
    ([[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4], 5),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    r, p, q = tree(*args)
    assert solution(r, p, q).val == expectation


def tree(a, pv, qv):
    root = TreeNode(a[0])
    i = 1
    q = deque([root])
    while q:
        node = q.popleft()

        if node.val == pv:
            pv = node
        elif node.val == qv:
            qv = node

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

    return root, pv, qv
