# flake8: noqa: F403, F405
import pytest
from leetcode.p0708_insert_into_a_sorted_circular_linked_list import *

solutions = [
    insort,
]

test_cases = [
    ([[3, 3, 3], 0], [3, 0, 3, 3]),
    ([[1, 3, 5], 0], [1, 3, 5, 0]),
    ([[3, 4, 1], 2], [3, 4, 1, 2]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    l, v = args
    assert to_arr(solution(to_list(l), v)) == expectation


def to_list(arr):
    head = Node(arr[0])

    curr = head
    for v in arr[1:]:
        curr.next = Node(v)
        curr = curr.next

    curr.next = head
    return head


def to_arr(lst):
    head = lst
    a = [head.val]
    curr = head.next

    while curr != head:
        a.append(curr.val)
        curr = curr.next

    return a
