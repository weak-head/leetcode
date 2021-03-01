# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p1650_lowest_common_ancestor_of_a_binary_tree_iii import *

solutions = [
    lowestCommonAncestor,
]

test_cases = [
    ([[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4], 5),
    ([[1, 2], 1, 2], 1),
    ([[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1], 3),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    root, p, q = tree(*args)
    assert solution(p, q).val == expectation


def tree(a, qv, pv):

    root = Node(a[0])
    q = deque([root])
    i = 1
    while q:
        node = q.popleft()

        if node.val == qv:
            qv = node
        elif node.val == pv:
            pv = node

        if i < len(a) and a[i] is not None:
            left = Node(a[i])
            node.left = left
            left.parent = node
            q.append(left)
        i += 1

        if i < len(a) and a[i] is not None:
            right = Node(a[i])
            node.right = right
            right.parent = node
            q.append(right)
        i += 1

    return root, pv, qv
