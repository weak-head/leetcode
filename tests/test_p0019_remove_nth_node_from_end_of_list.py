import pytest
from leetcode.p0019_remove_nth_node_from_end_of_list import removeNthFromEnd, ListNode


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


@pytest.mark.parametrize(('array', 'n', 'expectation'), (
    ([1,2,3,4,5], 1, [1,2,3,4]),
    ([1,2,3,4,5], 10, [1,2,3,4,5]),
    ([], 0, []),
    ([], 10, []),
    ([1,2,3,4,5], 2, [1,2,3,5]),
    ([1,2,3,4,5], 3, [1,2,4,5]),
    ([1,2,3,4,5], 4, [1,3,4,5]),
    ([1,2,3,4,5], 5, [2,3,4,5])
))
def test_removeNthFromEnd(array, n, expectation):
    head = removeNthFromEnd(to_list(array), n)
    result = list(from_list(head))

    assert result == expectation
