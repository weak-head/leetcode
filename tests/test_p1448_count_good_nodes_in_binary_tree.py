# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p1448_count_good_nodes_in_binary_tree import *

solutions = [
    goodNodes,
]

test_cases = [
    ([1, 2, 3, 4, 5, 6, 7], 7),
    ([1, None, 3, 1, 5], 3),
    ([1, 1, 1, 1, 1], 5),
    ([1, 2, 2, 3, 3, 3, 3, 2, 4, 4, 4, 4, 1, 2], 11),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(tree(args)) == expectation


def tree(a):
    root = TreeNode(val=a[0])
    q = deque([root])
    i = 1

    while q and i < len(a):
        node = q.popleft()

        if i < len(a) and a[i] is not None:
            node.left = TreeNode(val=a[i])
            q.append(node.left)
        i += 1

        if i < len(a) and a[i] is not None:
            node.right = TreeNode(val=a[i])
            q.append(node.right)
        i += 1

    return root
