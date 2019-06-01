import pytest
from leetcode.p0987_vertical_order_traversal_of_a_binary_tree import (
    verticalTraversal,
    TreeNode,
)


def to_tree(arr):
    def _to_tree(arr, ix, arrn):
        if ix >= arrn or arr[ix] is None:
            return None

        node = TreeNode(arr[ix])
        rix = (ix + 1) * 2
        lix = rix - 1
        node.left = _to_tree(arr, lix, arrn)
        node.right = _to_tree(arr, rix, arrn)

        return node

    return _to_tree(arr, 0, len(arr))


def to_arr(d):
    maxv = max(d.keys())
    arr = [None] * (maxv + 1)
    for k, v in d.items():
        arr[k] = v
    return arr


@pytest.mark.parametrize(
    ("tree", "expectation"),
    (
        ([3, 9, 20, None, None, 15, 7], [[9], [3, 15], [20], [7]]),
        ([1, 2, 3, 4, 5, 6, 7], [[4], [2], [1, 5, 6], [3], [7]]),
        (
            {
                0: 0,  # root
                1: 10,  # left child of: 0
                2: 1,  # right child of: 0
                4: 7,  # r: 10
                5: 2,  # l: 1
                6: 4,  # r: 1
                9: 3,  # l: 7
                12: 5,  # r: 2
                19: 6,  # l: 3
                26: 12,  # r: 5
                39: 8,  # l: 6
                54: 11,  # r: 12
                109: 9,  # l: 11
            },
            [[8], [6], [10, 3], [0, 2, 7], [1, 5], [4, 12, 9], [11]],
        ),
    ),
)
def test_verticalTraversal(tree, expectation):
    if isinstance(tree, dict):
        tree = to_arr(tree)
    t = to_tree(tree)
    assert verticalTraversal(t) == expectation
