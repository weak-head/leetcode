# flake8: noqa: F403, F405
import pytest
from leetcode.p0061_rotate_list import *

solutions = [
    rotateRight,
]

test_cases = [
    (([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3]),
    (([0, 1, 2], 4), [2, 0, 1]),
    (([0, 1, 2], 1), [2, 0, 1]),
    (([0], 100), [0]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    arr, k = args[0], args[1]
    assert from_list(solution(to_list(arr), k)) == expectation


def to_list(arr):
    head = curr = ListNode()
    for a in arr:
        curr.next = ListNode(a)
        curr = curr.next
    return head.next


def from_list(l):
    arr = []
    while l:
        arr.append(l.val)
        l = l.next
    return arr
