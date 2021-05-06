# flake8: noqa: F403, F405
import pytest
from leetcode.p0109_convert_sorted_list_to_binary_search_tree import *

solutions = [
    sortedListToBST_inorder,
    sortedListToBST_preorder,
]

test_cases = [
    (range(1), 1),
    (range(2), 2),
    (range(3), 2),
    (range(10), 4),
    (range(11), 4),
    (range(15), 4),
    (range(16), 5),
    (range(20), 5),
    (range(31), 5),
    (range(32), 6),
    (range(63), 6),
    (range(64), 7),
    (range(127), 7),
    (range(128), 8),
    (range(1023), 10),
    (range(1024), 11),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    args = list(args)
    lst = to_list(args)
    tree = solution(lst)
    assert height(tree, 0) == expectation
    assert inorder(tree) == args


def height(tree, h):
    if tree is None:
        return h
    return max(height(tree.left, h + 1), height(tree.right, h + 1))


def to_list(a):
    dummy = current = ListNode(None)
    for v in a:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


def inorder(tree):
    a = []

    def traverse(node):
        nonlocal a

        if node is None:
            return

        traverse(node.left)
        a.append(node.val)
        traverse(node.right)

    traverse(tree)
    return a
