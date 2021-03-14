class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapNodes(head: ListNode, k: int) -> ListNode:
    """
    This problem could be more complicated
    if we need to swap nodes, but not values.

    Time: O(n)
    Space: O(1)
        n - length of the list
    """
    cur = dummy = ListNode(None, head)

    while k != 1:
        cur = cur.next
        k -= 1

    pre_1 = cur
    pre_2 = dummy
    cur = cur.next

    while cur.next is not None:
        cur = cur.next
        pre_2 = pre_2.next

    if pre_1 == pre_2:
        return dummy.next

    # -- Swap value
    t = pre_1.next.val
    pre_1.next.val = pre_2.next.val
    pre_2.next.val = t

    # -- TBD: Or more complicated, swap nodes

    return dummy.next
