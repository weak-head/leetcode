class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swapPairs(head: ListNode) -> ListNode:
    new_head = current = ListNode(None)
    parent_prev = parent = None
    current.next, ix = head, 0

    while current.next is not None:
        parent_prev = parent
        parent = current
        current = current.next
        ix = ix + 1

        # even node
        if ix % 2 == 0:
            parent.next = current.next
            current.next = parent
            parent_prev.next = current
            current = parent

    return new_head.next


def swapPairs2(head: ListNode) -> ListNode:
    """More elegant solution"""
    if head is None or head.next is None:
        return head
    temp = head.next
    head.next = swapPairs2(temp.next)
    temp.next = head
    return temp
