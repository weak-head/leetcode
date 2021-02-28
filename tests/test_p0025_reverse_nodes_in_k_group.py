# flake8: noqa: F403, F405
import pytest
from typing import List, Generator
from leetcode.p0025_reverse_nodes_in_k_group import *

solutions = [
    reverseKGroup_optimized,
    reverseKGroup,
]


@pytest.mark.parametrize(
    ("list", "k", "result"),
    (
        ([], 1, []),
        ([], 110, []),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 100, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, [2, 1, 4, 3, 6, 5, 8, 7, 9]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [3, 2, 1, 6, 5, 4, 9, 8, 7]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 8, [8, 7, 6, 5, 4, 3, 2, 1, 9]),
    ),
)
@pytest.mark.parametrize("solution", solutions)
def test_reverse_nodes(list, k, result, solution):
    assert reverse_convert(list, k, solution) == result


def from_array(a: List[int]) -> ListNode:
    head = current = ListNode(None)
    for el in a:
        current.next = ListNode(el)
        current = current.next
    return head.next


def to_array(head: ListNode) -> Generator[int, None, None]:
    while head is not None:
        yield head.val
        head = head.next


def reverse_convert(a: List[int], k: int, f) -> List[int]:
    head = from_array(a)
    head = f(head, k)
    return list(to_array(head))
