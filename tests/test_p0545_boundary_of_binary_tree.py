from leetcode.p0545_boundary_of_binary_tree import (
    boundaryOfBinaryTree1,
    boundaryOfBinaryTree2,
    TreeNode,
)


def test_boundary():
    expectation = [1, 2, 4, 7, 8, 9, 10, 6, 3]

    tree = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(7), TreeNode(8))),
        TreeNode(3, TreeNode(6, TreeNode(9), TreeNode(10))),
    )

    assert list(boundaryOfBinaryTree1(tree)) == expectation
    assert list(boundaryOfBinaryTree2(tree)) == expectation
