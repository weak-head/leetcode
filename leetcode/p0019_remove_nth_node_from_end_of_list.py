class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    node, p_node, d_node, k = head, None, None, 1
    while node is not None:

        if d_node is None and k == n:
            d_node = head
        elif d_node is not None:
            p_node = d_node
            d_node = d_node.next

        node = node.next
        k = k + 1

    # generic case
    if p_node is not None:
        p_node.next = p_node.next.next
    # case when head is deleted
    elif d_node is not None:
        return d_node.next

    return head


def removeNthFromEnd2(head: ListNode, n: int) -> ListNode:
    if head is None:
        return None

    dummy = ListNode(None)
    dummy.next = head

    fast = slow = dummy
    for _ in range(n + 1):
        if fast is None:
            return head
        fast = fast.next

    while fast is not None:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next
