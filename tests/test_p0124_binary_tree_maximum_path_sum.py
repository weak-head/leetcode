# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p0124_binary_tree_maximum_path_sum import *

solutions = [
    maxPathSum,
]

#   ([args], expectation),
test_cases = [
    ([1, 2, 3], 6),
    ([-10, 9, 20, None, None, 15, 7], 42),
    ([2, -1, -2], 2),
    ([-1, -2, 10, -6, None, -3, -6], 10),
    ([-1, None, 9, -6, 3, None, None, None, -2], 12),
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
