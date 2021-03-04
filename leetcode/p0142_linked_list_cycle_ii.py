class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head: ListNode) -> ListNode:
    """
    First we need to detect if there is a cycle.
    We detect cycle using typical fast/slow pointers.
    The intersection of fast/slow is some node in the cycle.
    Then moving forward from the head and that point,
    we can detect start of the cycle.

    For example we have the following list with a cycle:

        1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 --
                    |                  |
                    --------------------

    Fast/slow moves:
        1 - 1
        2 - 3
        3 - 5
        4 - 7
        5 - 4
        6 - 6

    Node '6' is be the intersection point of the fast and slow pointers.
    Distance from "6" to the beginning of the cycle
    is same as distance from "1" to the beginning of cycle.

    So moving head/intersection:
        1 - 6
        2 - 7
        3 - 8
        4 - 4

    Results in detection of cycle start.

    Time: O(n)
    Space: O(1)
        n - number of nodes in the list
    """
    if not head:
        return None

    def intersection_point(head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return fast
        return None

    # detect some point of intersection
    # in the cycle
    intersection = intersection_point(head)
    if intersection is None:
        return None

    # detect start of the cycle
    p1 = head
    p2 = intersection
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next

    return p1
