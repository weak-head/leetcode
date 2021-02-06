import pytest
from collections import deque
from leetcode.p0199_binary_tree_right_side_view import (
    TreeNode,
    rightSideView,
)

test_cases = [
    #   (args, expectation)
    ([1, 2, 3, 4], [1, 3, 4]),
    ([1, None, 2, None, 5, 4, 6, 3], [1, 2, 5, 6, 3]),
    ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
def test_solve(args, expectation):
    t = tree(args)
    got = rightSideView(t)
    assert got == expectation


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
