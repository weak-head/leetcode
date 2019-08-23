import pytest
from typing import List, Generator
from leetcode.p0024_swap_nodes_in_pairs import swapPairs, swapPairs2, ListNode


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


def swap_convert(a: List[int], f) -> List[int]:
    head = from_array(a)
    head = f(head)
    return list(to_array(head))


@pytest.mark.parametrize(
    ("list", "swapped"),
    (
        ([], []),
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([1, 2, 3, 4, 5, 6, 7], [2, 1, 4, 3, 6, 5, 7]),
    ),
)
def test_swap(list, swapped):
    assert swap_convert(list, swapPairs) == swapped
    assert swap_convert(list, swapPairs2) == swapped
