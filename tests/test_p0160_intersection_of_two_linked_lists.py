# flake8: noqa: F403, F405
import pytest
from leetcode.p0160_intersection_of_two_linked_lists import *

solutions = [
    getIntersectionNode_fastslow,
    getIntersectionNode_math,
]

test_cases = [
    ([[1, 2, 3], [6, 7, 8], ["a", "b", "c"]], "a"),
    ([[1, 2, 3], [6, 7, 8], None], None),
    ([[1, 2, 3], [6, 7, 8], [9]], 9),
    ([None, None, [1, 2, 3]], 1),
    ([None, None, None], None),
    ([None, [1, 2], [3, 4]], 3),
    ([[1, 2], None, [3, 4]], 3),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    a, b = link(*args)
    node = solution(a, b)
    if expectation is None:
        assert node is None
    else:
        assert node.val == expectation


def link(a, b, c):
    hA = nA = ListNode(None)
    hB = nB = ListNode(None)
    hC = nC = ListNode(None)

    if a:
        for v in a:
            nA.next = ListNode(v)
            nA = nA.next

    if b:
        for v in b:
            nB.next = ListNode(v)
            nB = nB.next

    if c:
        for v in c:
            nC.next = ListNode(v)
            nC = nC.next

    nA.next = hC.next
    nB.next = hC.next

    return hA.next, hB.next
