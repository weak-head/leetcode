import pytest
from leetcode.p0141_linked_list_cycle import ListNode, hasCycle


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (([1, 2, 3, 4, 5], -1), (False)),
        (([1, 2, 3, 4, 5], 0), (True)),
        (([], -1), (False)),
        (([1], -1), (False)),
        (([1], 0), (True)),
        (([1, 2], 0), (True)),
        (([1, 2], 1), (True)),
        (([1, 2, 3], 0), (True)),
        (([1, 2, 3], 1), (True)),
        (([1, 2, 3], 2), (True)),
        (([1, 2, 3], -1), (False)),
        (([1, 2, 3, 4], 0), (True)),
        (([1, 2, 3, 4], 1), (True)),
        (([1, 2, 3, 4], 2), (True)),
        (([1, 2, 3, 4], 3), (True)),
        (([1, 2, 3, 4], -1), (False)),
    ),
)
def test_solve(a, expectation):
    l = listify(a[0], a[1])
    assert hasCycle(l) == expectation


def listify(a, cycle):
    cur = head = ListNode(None)
    for i in range(len(a)):
        cur.next = ListNode(a[i])
        cur = cur.next

    if cycle >= 0 and cycle < len(a):
        target = head.next
        for i in range(cycle):
            target = target.next
        cur.next = target

    return head.next
