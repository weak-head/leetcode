# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p0662_maximum_width_of_binary_tree import *

solutions = [
    widthOfBinaryTree,
]

test_cases = [
    ([1, 3, 2, 5, 3, None, 9], 4),
    ([1, 3, 2, 5, None, None, 9, 6, None, 7], 7),
    ([1, 3, 2, 5], 2),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(tree(args)) == expectation


def tree(a):
    if not a:
        return None

    root = TreeNode(a[0])
    q = deque([root])
    i = 1

    while q:
        node = q.popleft()

        if i < len(a) and a[i] is not None:
            node.left = TreeNode(a[i])
            q.append(node.left)
        i += 1

        if i < len(a) and a[i] is not None:
            node.right = TreeNode(a[i])
            q.append(node.right)
        i += 1

    return root
