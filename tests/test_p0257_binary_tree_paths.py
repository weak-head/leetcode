import pytest
from leetcode.p0257_binary_tree_paths import binaryTreePaths, TreeNode


def to_tree(arr):
    def _to_tree(arr, ix):
        if ix >= len(arr):
            return None
        rix = (ix + 1) * 2
        lix = rix - 1
        node = TreeNode(arr[ix])
        node.right = _to_tree(arr, rix)
        node.left = _to_tree(arr, lix)
        return node

    return _to_tree(arr, 0)


@pytest.mark.parametrize(
    ("tree", "paths"),
    (
        ([], []),
        ([5], ["5"]),
        ([7, 1], ["7->1"]),
        ([5, 3, 8, 1, 4, 7, 9], ["5->3->1", "5->3->4", "5->8->7", "5->8->9"]),
    ),
)
def test_binTree(tree, paths):
    assert binaryTreePaths(to_tree(tree)) == paths
