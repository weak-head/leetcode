# flake8: noqa: F403, F405
from typing import Deque
import pytest
from collections import deque
from leetcode.p0623_add_one_row_to_tree import *

solutions = [
    addOneRow,
]

test_cases = [
    ([[4, 2, 6, 3, 1, 5], 1, 2], [4, 1, 1, 2, None, None, 6, 3, 1, 5]),
    ([[2, 1, 3], 1, 1], [1, 2, None, 1, 3]),
    ([[2], 3, 2], [2, 3, 3]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    a, v, d = args
    t = tree(a)
    assert array(solution(t, v, d)) == expectation


def tree(a):
    root = TreeNode(a[0])
    q = deque([root])
    ix = 1
    while q:
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


def array(root):
    a = []
    q = deque([root])
    while q:
        node = q.popleft()

        if node is not None:
            a.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            a.append(None)

    while a and a[-1] is None:
        a.pop()

    return a
