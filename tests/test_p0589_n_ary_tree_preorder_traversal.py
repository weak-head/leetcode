# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p0589_n_ary_tree_preorder_traversal import *

solutions = [
    preorder,
]

test_cases = [
    (
        [
            1,
            None,
            2,
            3,
            4,
            5,
            None,
            None,
            6,
            7,
            None,
            8,
            None,
            9,
            10,
            None,
            None,
            11,
            None,
            12,
            None,
            13,
            None,
            None,
            14,
        ],
        [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10],
    ),
    ([1, None, 3, 2, 4, None, 5, 6], [1, 3, 5, 6, 2, 4]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(tree(args)) == expectation


def tree(a):
    root = Node(a[0], [])
    q = deque([root])
    i = 2
    while q:
        node = q.popleft()

        while i < len(a) and a[i] != None:
            c = Node(a[i], [])
            node.children.append(c)
            q.append(c)
            i += 1
        i += 1
    return root
