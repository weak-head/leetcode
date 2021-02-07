# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p0108_convert_sorted_array_to_binary_search_tree import *

solutions = [
    sortedArrayToBST,
]

#   ([args], expectation),
test_cases = [
    ([[-10, -3, 0, 5, 9]], [0, -10, 5, None, -3, None, 9]),
    ([[]], []),
    ([[0]], [0]),
    ([[1, 2, 3]], [2, 1, 3]),
    ([[1, 2, 3, 4, 5, 6, 7]], [4, 2, 6, 1, 3, 5, 7]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert array(solution(*args)) == expectation


def array(t):
    if not t:
        return []

    res = [t.val]
    q = deque([t])
    while q:
        node = q.popleft()

        if node.left:
            res.append(node.left.val)
            q.append(node.left)
        else:
            res.append(None)

        if node.right:
            res.append(node.right.val)
            q.append(node.right)
        else:
            res.append(None)

    # Drop redundant None elements from right
    while res[-1] is None:
        res.pop()

    return res
