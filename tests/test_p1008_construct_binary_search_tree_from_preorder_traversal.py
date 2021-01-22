import pytest
from leetcode.p1008_construct_binary_search_tree_from_preorder_traversal import (
    TreeNode,
    bstFromPreorder,
    bstFromPreorder2,
)


def inorder(node: TreeNode):
    if node is not None:
        if node.left:
            for x in inorder(node.left):
                yield x

        yield node.val

        if node.right:
            for x in inorder(node.right):
                yield x


@pytest.mark.parametrize(
    ("preorder", "tree"),
    (
        ([8, 5, 1, 7, 10, 12], [1, 5, 7, 8, 10, 12]),
        ([7, 1, 0, 3, 2, 5, 4, 6, 9, 8, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ([10, 5, 3, 1, 2, 7, 15, 11, 17, 19], [1, 2, 3, 5, 7, 10, 11, 15, 17, 19]),
    ),
)
def test_bst(preorder, tree):
    assert list(inorder(bstFromPreorder(preorder))) == tree
    assert list(inorder(bstFromPreorder2(preorder))) == tree
