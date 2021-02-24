# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p0337_house_robber_iii import *

solutions = [
    rob,
]

test_cases = [
    ([3, 2, 3, None, 3, None, 1], 7),
    ([3, 3, 3, None, 3, None, 3], 9),
    ([3, 3, 3, 3, 3, 3, 3], 15),
    ([1, None, None], 1),
    ([1, 2, None], 2),
    ([1, None, 3], 3),
    ([3, 1, 1], 3),
    ([2, 3, 1], 4),
    ([], 0),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(tree(args)) == expectation


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
