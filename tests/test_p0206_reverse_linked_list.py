import pytest
from leetcode.p0206_reverse_linked_list import ListNode, reverseList, reverseListRec


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        ([1], [1]),
        ([1, 2, 3], [3, 2, 1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ),
)
@pytest.mark.parametrize("solution", [reverseListRec, reverseList])
def test_solve(a, expectation, solution):
    p1, p2 = to_list(expectation), solution(to_list(a))
    while p1 is not None and p2 is not None:
        assert p1.val == p2.val
        p1 = p1.next
        p2 = p2.next


def to_list(a):
    cur = head = ListNode(a[0])
    for i in range(1, len(a)):
        cur.next = ListNode(a[i])
        cur = cur.next
    return head
