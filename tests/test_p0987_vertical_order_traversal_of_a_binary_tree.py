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


@pytest.mark.parametrize(
    ("tree", "expectation"),
    (
        ([3, 9, 20, None, None, 15, 7], [[9], [3, 15], [20], [7]]),
        ([1, 2, 3, 4, 5, 6, 7], [[4], [2], [1, 5, 6], [3], [7]]),
        (
            [
                0,
                10,
                1,
                None,
                None,
                2,
                4,
                3,
                5,
                None,
                None,
                6,
                None,
                7,
                9,
                8,
                None,
                None,
                None,
                None,
                11,
                None,
                None,
                12,
            ],
            [[8], [6], [10, 3], [0, 2, 7], [1, 5], [4, 9, 12], [11]],
        ),
    ),
)
def test_verticalTraversal(tree, expectation):
    t = to_tree(tree)
    assert verticalTraversal(t) == expectation
