# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p0538_convert_bst_to_greater_tree import *

solutions = [
    convertBST,
]

#   ([args], expectation),
test_cases = [
    (
        [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8],
        [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8],
    )
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert array(solution(tree(args))) == expectation


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
