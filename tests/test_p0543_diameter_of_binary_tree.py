# flake8: noqa: F403, F405
import pytest
from collections import deque
from leetcode.p0543_diameter_of_binary_tree import *

solutions = [
    diameterOfBinaryTree,
]

test_cases = [
    ([1, 2, 3, 4, 5], 3),
    ([1, 2], 1),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 7),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(tree(args)) == expectation


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree(a):
    root = Node(val=a[0])
    q = deque([root])
    i = 1

    while q and i < len(a):
        node = q.popleft()

        if i < len(a) and a[i] is not None:
            node.left = Node(val=a[i])
            q.append(node.left)
        i += 1

        if i < len(a) and a[i] is not None:
            node.right = Node(val=a[i])
            q.append(node.right)
        i += 1

    return root
