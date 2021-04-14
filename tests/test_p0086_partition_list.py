# flake8: noqa: F403, F405
import pytest
from leetcode.p0086_partition_list import *

solutions = [
    partition,
]

test_cases = [
    ([[1, 2, 3, 4, 5, 6], 7], [1, 2, 3, 4, 5, 6]),
    ([[1, 2, 3, 4, 5, 6], 1], [1, 2, 3, 4, 5, 6]),
    ([[1, 2, 3, 4, 5, 6], 4], [1, 2, 3, 4, 5, 6]),
    ([[4, 5, 6, 3, 1, 2], 3], [1, 2, 4, 5, 6, 3]),
    ([[1, 2, 3, 4, 2, 6], 3], [1, 2, 2, 3, 4, 6]),
    ([[1, 4, 3, 2, 5, 2], 3], [1, 2, 2, 4, 3, 5]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    a, v = args
    assert to_array(solution(to_list(a), v)) == expectation


def to_list(a):
    dummy = cur = ListNode()
    for v in a:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_array(l):
    a = []
    while l:
        a.append(l.val)
        l = l.next
    return a
