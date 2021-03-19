# flake8: noqa: F403, F405
import pytest
from leetcode.p0876_middle_of_the_linked_list import *

solutions = [
    middleNode,
]

test_cases = [
    ([], None),
    ([1, 2, 3, 4, 5], 3),
    ([1, 2, 3, 4, 5, 6], 4),
    ([1], 1),
    ([1, 2], 2),
    ([1, 2, 3], 2),
    ([1, 2, 3, 4], 3),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    if expectation is not None:
        assert solution(to_list(args)).val == expectation
    else:
        assert solution(to_list(args)) is None


def to_list(a):
    cur = dummy = ListNode(None)
    for v in a:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next
