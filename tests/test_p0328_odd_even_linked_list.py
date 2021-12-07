# flake8: noqa: F403, F405
import pytest
from leetcode.p0328_odd_even_linked_list import *

solutions = [
    oddEvenList,
]

test_cases = [
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]),
    ([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):

    assert from_list(solution(to_list(args))) == expectation


def to_list(arr):
    c = h = ListNode(None)
    for a in arr:
        c.next = ListNode(a)
        c = c.next
    return h.next


def from_list(head):
    a = []
    while head:
        a.append(head.val)
        head = head.next
    return a
