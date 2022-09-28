# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p0863_all_nodes_distance_k_in_binary_tree import *

solutions = [
    distanceK,
]

test_cases = [
    ([[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 2], [7, 4, 1]),
    ([[1], 1, 3], []),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    arr = args[0]
    target = args[1]
    k = args[2]
    r, t = tree(arr, target)

    assert set(solution(r, t, k)) == set(expectation)


def tree(a, t):

    root = TreeNode(a[0])
    i = 1
    target = None
    q = deque([root])

    while q:
        node = q.popleft()

        if node.val == t:
            target = node

        if i < len(a) and a[i] is not None:
            node.left = TreeNode(a[i])
            q.append(node.left)
        i += 1

        if i < len(a) and a[i] is not None:
            node.right = TreeNode(a[i])
            q.append(node.right)
        i += 1

    return root, target
