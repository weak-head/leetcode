import pytest
from leetcode.p0021_merge_two_sorted_lists import ListNode, merge, mergeTwoLists


def to_list(array):
    head = node = ListNode(None)
    for itm in array:
        node.next = ListNode(itm)
        node = node.next
    return head.next


def from_list(head):
    while head != None:
        yield head.val
        head = head.next


@pytest.mark.parametrize(('a', 'b', 'res'), (
    ([], [], []),
    ([], [1], [1]),
    ([1], [], [1]),
    ([1,2], [], [1,2]),
    ([1,2,3,4,6], [5], [1,2,3,4,5,6]),
    ([1, 5], [2,3,4,6], [1,2,3,4,5,6]),
    ([1,3,5,7], [2,4,6], [1,2,3,4,5,6,7])
))
def test_merge(a, b, res):
    head1 = merge(to_list(a), to_list(b))
    head2 = mergeTwoLists(to_list(a), to_list(b))
    assert list(from_list(head1)) == res
    assert list(from_list(head2)) == res