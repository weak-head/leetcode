# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p0098_validate_binary_search_tree import *

solutions = [
    isValidBST,
]

#   ([args], expectation),
test_cases = [
    ([5, 4, 6, None, None, 3, 7], False),
    ([3, None, 30, 10, None, None, 15, None, 45], False),
    ([2, 1, 3], True),
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
