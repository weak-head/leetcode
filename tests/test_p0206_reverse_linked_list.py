import pytest
from leetcode.p0206_reverse_linked_list import ListNode, reverseList


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        ((ListNode(1)), (ListNode(1))),
        (
            (ListNode(1, ListNode(2, ListNode(3)))),
            (ListNode(3, ListNode(2, ListNode(1)))),
        ),
    ),
)
def test_solve(a, expectation):
    r = reverseList(a)
    p1, p2 = expectation, r
    while p1 is not None and p2 is not None:
        assert p1.val == p2.val
        p1 = p1.next
        p2 = p2.next
