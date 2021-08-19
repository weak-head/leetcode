# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p1339_maximum_product_of_splitted_binary_tree import *

solutions = [
    maxProduct,
]

test_cases = [
    ([1, 2, 3, 4, 5, 6], 110),
    ([1, None, 2, 3, 4, None, None, 5, 6], 90),
    ([2, 3, 9, 10, 7, 8, 6, 5, 4, 11, 1], 1025),
    ([1, 1], 1),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(tree(args)) == expectation


def tree(a):
    root = TreeNode(val=a[0])
    ix = 1
    q = deque([root])

    while q and ix < len(a):
        node = q.popleft()

        if ix < len(a) and a[ix] is not None:
            node.left = TreeNode(val=a[ix])
            q.append(node.left)
        ix += 1

        if ix < len(a) and a[ix] is not None:
            node.right = TreeNode(val=a[ix])
            q.append(node.right)
        ix += 1

    return root
