# flake8: noqa: F403, F405
import pytest
from leetcode.p1721_swapping_nodes_in_a_linked_list import *

solutions = [
    swapNodes,
]

test_cases = [
    ([[1, 2, 3, 4, 5], 2], [1, 4, 3, 2, 5]),
    ([[7, 9, 6, 6, 7, 8, 3, 0, 9, 5], 5], [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]),
    ([[1, 2, 3], 2], [1, 2, 3]),
    ([[1, 2, 3, 4, 5], 1], [5, 2, 3, 4, 1]),
    ([[1], 1], [1]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    a, k = args
    assert to_array(solution(to_list(a), k)) == expectation


def to_array(l):
    a = []
    while l is not None:
        a.append(l.val)
        l = l.next
    return a


def to_list(a):
    dummy = cur = ListNode(None)
    for v in a:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next
