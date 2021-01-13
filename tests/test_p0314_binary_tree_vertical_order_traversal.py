import pytest
from leetcode.p0314_binary_tree_vertical_order_traversal import TreeNode, verticalOrder


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (
            (
                TreeNode(
                    3,
                    TreeNode(9, TreeNode(4), TreeNode(0, right=TreeNode(2))),
                    TreeNode(8, TreeNode(1, TreeNode(5)), TreeNode(7)),
                )
            ),
            ([[4], [9, 5], [3, 0, 1], [8, 2], [7]]),
        ),
    ),
)
def test_order(a, expectation):
    assert verticalOrder(a) == expectation
