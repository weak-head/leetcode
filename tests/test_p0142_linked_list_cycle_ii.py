# flake8: noqa: F403, F405
import pytest
from leetcode.p0142_linked_list_cycle_ii import *

solutions = [
    detectCycle,
]

test_cases = [
    ([[1, 2, 3, 4, 5, 6, 7, 8], 0], 1),
    ([[1, 2, 3, 4, 5, 6, 7, 8], 3], 4),
    ([[1, 2, 3, 4, 5, 6, 7, 8], None], None),
    ([[1, 2, 3, 4, 5, 6, 7, 8], 7], 8),
    ([[1, 2, 3, 4, 5, 6, 7, 8], 6], 7),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    h = link(*args)
    node = solution(h)
    if expectation is None:
        assert node is None
    else:
        assert node.val == expectation


def link(a, ix):
    dummy = node = ListNode(None)
    cycle = None
    for i in range(len(a)):
        node.next = ListNode(a[i])
        node = node.next
        if i == ix:
            cycle = node
    node.next = cycle
    return dummy.next
