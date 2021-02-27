# flake8: noqa: F403, F405
import pytest
from leetcode.p0092_reverse_linked_list_ii import *

solutions = [
    reverseBetween,
]

test_cases = [
    ([[1, 2, 3], 1, 1], [1, 2, 3]),
    ([[1, 2, 3, 4, 5], 2, 4], [1, 4, 3, 2, 5]),
    ([[1, 2, 3, 4, 5], 1, 4], [4, 3, 2, 1, 5]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    head, l, r = args
    head = to_list(head)

    assert to_arr(solution(head, l, r)) == expectation


def to_list(a):
    cur = head = ListNode(a[0])
    for i in range(1, len(a)):
        cur.next = ListNode(a[i])
        cur = cur.next
    return head


def to_arr(head):
    a = []
    while head:
        a.append(head.val)
        head = head.next
    return a
