# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p0095_unique_binary_search_trees_ii import *

solutions = [
    generateTrees,
]

test_cases = [
    (1, [[1]]),
    (2, [[1, None, 2], [2, 1]]),
    (
        3,
        [
            [1, None, 2, None, 3],
            [1, None, 3, 2],
            [2, 1, 3],
            [3, 1, None, None, 2],
            [3, 2, None, 1],
        ],
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert list(map(to_a, solution(args))) == expectation


def to_a(root):
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

    while a[-1] is None:
        a.pop()

    return a
