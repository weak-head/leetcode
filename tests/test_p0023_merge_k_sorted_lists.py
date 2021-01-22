import pytest
from leetcode.p0023_merge_k_sorted_lists import mergeKLists, mergeKLists_pq, ListNode


def to_list(array):
    head = node = ListNode(None)
    for itm in array:
        node.next = ListNode(itm)
        node = node.next
    return head.next


def from_list(head):
    while head is not None:
        yield head.val
        head = head.next


@pytest.mark.parametrize(
    ("lists", "result"),
    (
        ([], []),
        ([[], [], []], []),
        ([[1, 3, 6], [2, 4, 7], [5, 8]], [1, 2, 3, 4, 5, 6, 7, 8]),
        ([[], [], [1]], [1]),
        ([[], [1], []], [1]),
        ([[1], [], []], [1]),
        ([[1, 2, 3], [], [0]], [0, 1, 2, 3]),
        ([[0], [1, 2, 3], []], [0, 1, 2, 3]),
        ([[0], [], [1, 2, 3]], [0, 1, 2, 3]),
        ([[], [0], [1, 2, 3]], [0, 1, 2, 3]),
    ),
)
def test_merge(lists, result):
    head1 = mergeKLists([to_list(k) for k in lists])
    head2 = mergeKLists_pq([to_list(k) for k in lists])
    assert list(from_list(head1)) == result
    assert list(from_list(head2)) == result
