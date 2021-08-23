# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p0653_two_sum_iv_input_is_a_bst import *

solutions = [
    findTarget,
]

test_cases = [
    ([[5, 3, 6, 2, 4, None, 7], 9], True),
    ([[5, 3, 6, 2, 4, None, 7], 28], False),
    ([[2, 1, 3], 4], True),
    ([[2, 1, 3], 1], False),
    ([[2, 1, 3], 3], True),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    a, k = args
    assert solution(tree(a), k) == expectation


def tree(a):
    root = TreeNode(val=a[0])
    q = deque([root])
    ix = 1

    while q:
        node = q.popleft()

        if ix < len(a) and a[ix] is not None:
            node.left = TreeNode(val=a[ix])
            q.append(node.left)
        ix += 1

        if ix < len(a) and a[ix] is not None:
            node.right = TreeNode(val=a[ix])
            q.append(node.right)
        ix += 1

    return root
