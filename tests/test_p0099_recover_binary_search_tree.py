# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p0099_recover_binary_search_tree import *

solutions = [
    recoverTree_inorder,
    recoverTree_morris,
]

#   ([args], expectation),
test_cases = [
    ([4, 20, 3, None, None, 15, 22], [4, 3, 20, None, None, 15, 22]),
    ([5, 3, 9, 4, 1, 7, 11], [5, 3, 9, 1, 4, 7, 11]),
    (
        [5, 3, 6, 1, 4, 7, 11, None, None, None, None, 9, 8],
        [5, 3, 9, 1, 4, 7, 11, None, None, None, None, 6, 8],
    ),
    ([3, 1, 4, None, None, 2], [2, 1, 4, None, None, 3]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    t = tree(args)
    solution(t)
    assert array(t) == expectation


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
