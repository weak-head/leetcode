import pytest
from collections import deque
from leetcode.p0669_trim_a_binary_search_tree import TreeNode, trimBST


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (
            (
                [3, 0, 4, None, 2, None, None, 1],
                1,
                3,
            ),
            ([3, 2, None, 1]),
        ),
        (([1], 1, 2), ([1])),
        (
            (
                [5, 3, 8, 1, 4, 7, 12],
                1,
                15,
            ),
            ([5, 3, 8, 1, 4, 7, 12]),
        ),
        (
            (
                [5, 3, 8, 1, 4, 7, 12],
                1,
                7,
            ),
            ([5, 3, 7, 1, 4]),
        ),
    ),
)
def test_solve(a, expectation):
    t = tree(a[0])
    trimmed = trimBST(t, a[1], a[2])
    assert array(trimmed) == expectation


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
