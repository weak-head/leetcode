# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p0450_delete_node_in_a_bst import *

solutions = [
    deleteNode,
]

test_cases = [
    ([[5, 3, 6, 2, 4, None, 7], 3], [5, 4, 6, 2, None, None, 7]),
    ([[5, 3, 6, 2, 4, None, 7], 0], [5, 3, 6, 2, 4, None, 7]),
    ([[3, 1, 4], 1], [3, None, 4]),
    ([[3, 1, 4], 4], [3, 1]),
    ([[3, 1, 4], 3], [4, 1]),
    ([[], 1], []),
    ([[20, 5, 40], 21], [20, 5, 40]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    a, key = args
    assert array(solution(tree(a), key)) == expectation


def tree(a):
    if not a:
        return None

    root = TreeNode(a[0])
    i = 1
    q = deque([root])
    while q:
        node = q.popleft()

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
    return root


def array(t):
    if t is None:
        return []

    a = []
    q = deque([t])
    while q:
        node = q.popleft()

        if node is not None:
            a.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            a.append(None)

    while a[-1] is None:
        a.pop()

    return a
