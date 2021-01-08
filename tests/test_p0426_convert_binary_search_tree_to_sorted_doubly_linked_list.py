from leetcode.p0426_convert_binary_search_tree_to_sorted_doubly_linked_list import (
    Node,
    treeToDoublyList,
)


def test_tree():
    input = Node(4, Node(2, Node(1), Node(3)), Node(5))
    input = treeToDoublyList(input)

    node = input
    for i in [1, 2, 3, 4, 5, 1]:
        assert node.val == i
        node = node.right

    node = input
    for i in [1, 5, 4, 3, 2, 1, 5]:
        assert node.val == i
        node = node.left
